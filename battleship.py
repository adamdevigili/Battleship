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
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

#Game baord variables
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

#Color definitions
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
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


class Ship:
    size = None #PT Boat = 2, Destroyer = 3, Submarine = 3, Battleship = 4, Carrier = 5
    orient = None
    loc = (None, None)
    hit_list = []

class PTBoat(Ship):
    def __init__(self, orient, loc):
        self.size=2
        self.hit_list = [0, 0]
        self.orient = orient
        self.loc = loc

class Destroyer(Ship):
    def __init__(self, orient, loc):
        self.size=3
        self.hit_list = [0, 0, 0]
        self.orient = orient
        self.loc = loc

class Submarine(Ship):
    def __init__(self, orient, loc):
        self.size=3
        self.hit_list = [0, 0, 0]
        self.orient = orient
        self.loc = loc

class Battleship(Ship):
    def __init__(self, orient, loc):
        self.size=4
        self.hit_list = [0, 0, 0, 0]
        self.orient = orient
        self.loc = loc

class Carrier(Ship):
    def __init__(self, orient, loc):
        self.size=5
        self.hit_list = [0, 0, 0, 0, 0]
        self.orient = orient
        self.loc = loc


def main():
    global fpsClock, screen
    screen.fill(WHITE)

    #Background music
    pygame.mixer.music.play(-1)

    pygame.display.set_caption('Battleship')

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event

    player_board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
    opp_board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

    for row in player_board:
        print row
    while True: # the main game loop
        mouseClicked = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        if mouseClicked:
            gun_sound.play()

        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    main()
