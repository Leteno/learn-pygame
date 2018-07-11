#!/usr/bin/env python3

import pygame
from pygame.locals import *

from gamestate import *
from scene import welcome_scene, config_scene
from scene.game import game_scene

WINDOWWIDTH = 550
WINDOWHEIGHT = 400

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    FPSCLOCK = pygame.time.Clock()
    DATA = game_data()
    pygame.display.set_caption('Card Game')

    gameState = GAME
    while True:
        if gameState == WELCOME :
            gameState = welcome_scene.runGame(DISPLAYSURF, FPSCLOCK, DATA)
        elif gameState == CONFIG :
            gameState = config_scene.runGame(DISPLAYSURF, FPSCLOCK, DATA)
        elif gameState == GAME :
            gameState = game_scene.runGame(DISPLAYSURF, FPSCLOCK, DATA)
        else :
            print('game loop ends up here')
            break

if __name__ == '__main__' :
    main()
