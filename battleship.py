#!/usr/bin/env python
#############################
# Filename: battleship.py
# Author: Adamo Devigili
# Website: adamdevigili.com
# Date: April 15, 2017
#############################

import pygame, sys
from pygame.locals import *
from os import path

##### CONSTANTS #####
#Window Variables
FPS = 30
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

#Game baord variables
BOARD_SIZE = 500
BOARD_WIDTH = 10
BOARD_HEIGHT = 10
BOARD_START_X = 30
BOARD_START_Y = 30

SQUARE_SIZE = (BOARD_SIZE-(BOARD_SIZE/10))/10
SPACING = SQUARE_SIZE/10

#Color definitions
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
NAVY = (60, 60, 160)
###################

##### INIT/LOAD #####
pygame.init()
pygame.mixer.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

image_folder = path.join(path.dirname(__file__), 'images')
sound_folder = path.join(path.dirname(__file__), 'sounds')

background_music = pygame.mixer.music.load('sounds/ocean-background.mp3')
gun_sound = pygame.mixer.Sound(path.join(sound_folder,'sounds/fire-gun.mp3'))

###############


def main():
    global fpsClock, screen
    screen.fill(NAVY)

    place_ships_phase = True
    ships_to_place = ["carrier", "battleship", "subarine", "destroyer", "ptboat"]
    #Background music
    #pygame.mixer.music.play(-1)

    pygame.display.set_caption('Battleship')

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event

    player_board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
    opp_board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

    player_rect_board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
    for row in range(BOARD_WIDTH):
        for column in range(BOARD_HEIGHT):
            player_rect_board[row][column] = Rect([(SPACING + SQUARE_SIZE) * column + SPACING, (SPACING + SQUARE_SIZE) * row + SPACING,SQUARE_SIZE, SQUARE_SIZE])

    #pygame.draw.rect(screen, BLACK, (BOARD_START_X, BOARD_START_Y, BOARD_SIZE, BOARD_SIZE))
    mousePos = (0, 0)

    while True: # the main game loop
        mouseClicked = False

        if not ships_to_place:  #If all ships have been placed
            place_ships_phase = False



        if place_ships_phase:
            current_ship = ships_to_place[0]
            print current_ship
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mousePos = event.pos
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    ships_to_place.remove(current_ship)
                    mousePos = event.pos
                    mouseClicked = True

            if mouseClicked:
                gun_sound.play()

            print mousePos

            for row in range(BOARD_WIDTH):
                for column in range(BOARD_HEIGHT):
                    r = player_rect_board[row][column]
                    if r.collidepoint(mousePos):
                        color = RED
                    else:
                        color = WHITE
                    pygame.draw.rect(screen, color, r)

            pygame.display.update()
            fpsClock.tick(FPS)
        else:
            print "Now in play state"
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mousePos = event.pos
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    mousePos = event.pos
                    mouseClicked = True



def place_ship(player_rect_board, ship):
    pass

class Tile:
    pos_x = None
    pos_y = None
class Ship:
    name = None
    size = None #PT Boat = 2, Destroyer = 3, Submarine = 3, Battleship = 4, Carrier = 5
    orient = None
    loc = (None, None)

    tile_list = []
    hit_list = []

    def check_alive():
        if 0 not in hit_list:   #every part was hit_list
            return False
        else:
            return True

class PTBoat(Ship):
    def __init__(self, orient, loc):
        self.name="PT Boat"
        self.size=2
        self.hit_list = [0, 0]
        self.orient = orient
        self.loc = loc

class Destroyer(Ship):
    def __init__(self, orient, loc):
        self.name="Destroyer"
        self.size=3
        self.hit_list = [0, 0, 0]
        self.orient = orient
        self.loc = loc

class Submarine(Ship):
    def __init__(self, orient, loc):
        self.name="Submarine"
        self.size=3
        self.hit_list = [0, 0, 0]
        self.orient = orient
        self.loc = loc

class Battleship(Ship):
    def __init__(self, orient, loc):
        self.name="Battleship"
        self.size=4
        self.hit_list = [0, 0, 0, 0]
        self.orient = orient
        self.loc = loc

class Carrier(Ship):
    def __init__(self, orient, loc):
        self.name="Aircraft Carrier"
        self.size=5
        self.hit_list = [0, 0, 0, 0, 0]
        self.orient = orient
        self.loc = loc


if __name__ == '__main__':
    main()
