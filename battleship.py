#!/usr/bin/env python
#############################
# Filename: battleship.py
# Author: Adamo Devigili
# Date: April 15, 2017
#############################

import pygame, sys
from pygame.locals import *

FPS = 30 # frames per second setting
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BOARD_WIDTH = 10
BOARD_HEIGHT = 10


RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)


fpsClock = pygame.time.Clock()

pygame.init()
# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Battleship')

WHITE = (255, 255, 255)

# Loading and playing background music:
pygame.mixer.music.load('sounds/Edge-of-Ocean_Looping.mp3')
pygame.mixer.music.play(-1, 0.0)

DISPLAYSURF.fill(WHITE)
while True: # the main game loop


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
