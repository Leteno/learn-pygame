#!/usr/bin/env python3

import pygame
from pygame.locals import *

from gamestate import WELCOME, CONFIG, CHARACTER, EXIT, FPS
from util import *
import color

def runGame(surface, clock):
    print('showing welcome scene')
    w = surface.get_width()
    h = surface.get_height()
    half_w = int(w / 2)
    half_h = int(h / 2)
    font = pygame.font.Font('freesansbold.ttf', 32)
    titleSurf = font.render('CardGame', 1, color.YELLOW)
    titleRect = titleSurf.get_rect()
    startGameSurf = font.render('Start Game', 1, color.WHITE)
    startGameRect = startGameSurf.get_rect()
    configSurf = font.render('Configuration', 1, color.WHITE)
    configRect = configSurf.get_rect()
    exitGameSurf = font.render('Exit Game', 1, color.WHITE)
    exitGameRect = exitGameSurf.get_rect()

    one_fifth_w = int(w / 5)
    one_fifth_h = int(h / 5)
    titleRect.center = (one_fifth_w, one_fifth_h)
    startGameRect.center = (one_fifth_w * 2, one_fifth_h * 2)
    configRect.center = (one_fifth_w * 3, one_fifth_h * 3)
    exitGameRect.center = (one_fifth_w * 4, one_fifth_h * 4)
    

    while True :
        # terminate when esc
        checkForQuit()
        # handle click event
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if startGameRect.collidepoint(event.pos) :
                    print('click on start game')
                    return CHARACTER
                elif configRect.collidepoint(event.pos) :
                    print('click on config')
                    return CONFIG
                elif exitGameRect.collidepoint(event.pos) :
                    print('click on exit game')
                    return EXIT
        # show 'start game' 'configuration' 'exit game'
        surface.fill(color.MAINCOLOR)
        surface.blit(titleSurf, titleRect)
        surface.blit(startGameSurf, startGameRect)
        surface.blit(configSurf, configRect)
        surface.blit(exitGameSurf, exitGameRect)
        pygame.display.update()
        clock.tick(FPS)


