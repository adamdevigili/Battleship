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
BOARD_START_Y = 50

OPP_BOARD_OFFSET = 650


SQUARE_SIZE = (BOARD_SIZE-(BOARD_SIZE/10))/10
SPACING = SQUARE_SIZE/10

#Color definitions
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
NAVY = (60, 60, 160)
ORANGE = (255, 165, 0)
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

    carrier = Carrier()

    ships_to_place = ["carrier", "battleship", "subarine", "destroyer", "ptboat"]
    #Background music
    #pygame.mixer.music.play(-1)

    pygame.display.set_caption('Battleship')

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event


    # 0 -> nothing in this square, WHITE
    # 1 -> player's ship in this square, GRAY
    # 2 -> missed shot for either player, BLUE
    # 3 -> hit shot for either player, ORANGE
    # 4 -> completely knocked out ship, RED

    player_game_board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
    opp_game_board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

    player_rect_board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
    for row in range(BOARD_WIDTH):
        for column in range(BOARD_HEIGHT):
            player_rect_board[row][column] = Rect([(SPACING + SQUARE_SIZE) * column + SPACING + BOARD_START_X, (SPACING + SQUARE_SIZE) * row + SPACING + BOARD_START_Y, SQUARE_SIZE, SQUARE_SIZE])

    opp_rect_board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
    for row in range(BOARD_WIDTH):
        for column in range(BOARD_HEIGHT):
            opp_rect_board[row][column] = Rect([(SPACING + SQUARE_SIZE) * column + SPACING + OPP_BOARD_OFFSET + BOARD_START_X, (SPACING + SQUARE_SIZE) * row + SPACING + BOARD_START_Y, SQUARE_SIZE, SQUARE_SIZE])

    pygame.draw.rect(screen, BLACK, (WINDOW_WIDTH/2, 0, 10, WINDOW_HEIGHT))     #Middle line

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
                    #ships_to_place.remove(current_ship)
                    mousePos = event.pos
                    mouseClicked = True


            print mousePos

            for row in range(BOARD_WIDTH):
                for column in range(BOARD_HEIGHT):
                    r = player_rect_board[row][column]
                    if r.collidepoint(mousePos) and event.type == MOUSEBUTTONDOWN:
                        #color = GRAY
                        player_game_board[row][column] += 1
                    #elif:
                        #color = WHITE
                    if player_game_board[row][column] == 0:
                        color = WHITE
                    elif player_game_board[row][column] == 1:
                        color = GRAY
                    elif player_game_board[row][column] == 2:
                        color = BLUE
                    elif player_game_board[row][column] == 3:
                        color = ORANGE
                    elif player_game_board[row][column] == 4:
                        color = RED

                    pygame.draw.rect(screen, color, r)

            for row in range(BOARD_WIDTH):
                for column in range(BOARD_HEIGHT):
                    r = opp_rect_board[row][column]
                    if r.collidepoint(mousePos) and event.type == MOUSEBUTTONDOWN:
                        #color = GRAY
                        opp_game_board[row][column] += 1
                    #elif:
                        #color = WHITE
                    if opp_game_board[row][column] == 0:
                        color = WHITE
                    elif opp_game_board[row][column] == 1:
                        color = GRAY
                    elif opp_game_board[row][column] == 2:
                        color = BLUE
                    elif opp_game_board[row][column] == 3:
                        color = ORANGE
                    elif opp_game_board[row][column] == 4:
                        color = RED

                    pygame.draw.rect(screen, color, r)

            pygame.display.update()
            fpsClock.tick(FPS)
        else:   #Play phase
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

            if mouseClicked:
                gun_sound.play()


def place_ship(player_rect_board, ship):
    pass

class Tile:
    pos_x = None
    pos_y = None

#Parent class for all ships
class Ship(pygame.sprite.Sprite):
    name = None
    size = None         #PT Boat = 2, Destroyer = 3, Submarine = 3, Battleship = 4, Carrier = 5
    orient = None       #up, down, left, right
    loc = (None, None)

    tile_list = []      #List of coordinates that the ship is placed on
    hit_list = []       #List of current hits taken status. 0 is no hit, 1 is hit

    def get_tiles(self):
        pass



    def check_alive():
        if 0 not in hit_list:   #every part of the ship was hit, therefore it is dead
            return False
        else:
            return True

class PTBoat(Ship):
    def __init__(self):
        self.name="PT Boat"
        self.size=2
        self.hit_list = [0, 0]
        self.orient = orient
        self.loc = loc

class Destroyer(Ship):
    def __init__(self):
        self.name="Destroyer"
        self.size=3
        self.hit_list = [0, 0, 0]
        self.orient = orient
        self.loc = loc

class Submarine(Ship):
    def __init__(self):
        self.name="Submarine"
        self.size=3
        self.hit_list = [0, 0, 0]
        self.orient = orient
        self.loc = loc

class Battleship(Ship):
    def __init__(self):
        self.name="Battleship"
        self.size=4
        self.hit_list = [0, 0, 0, 0]
        self.orient = orient
        self.loc = loc

class Carrier(Ship):
    def __init__(self):
        self.name="Aircraft Carrier"
        self.size=5
        self.hit_list = [0, 0, 0, 0, 0]
        #self.orient = orient
        #self.loc = loc


if __name__ == '__main__':
    main()
