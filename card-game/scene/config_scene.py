#!/usr/bin/env python3

import pygame
from pygame.locals import *

from gamestate import WELCOME, CONFIG, FPS
from util import *
import color

def runGame(surface, clock):
    print('showing config scene')
    w = surface.get_width()
    h = surface.get_height()
    half_w = int(w / 2)
    half_h = int(h / 2)
    font = pygame.font.Font('freesansbold.ttf', 24)
    titleSurf = font.render('Configuration', 1, color.BLUE)
    titleRect = titleSurf.get_rect()
    titleRect.center = (half_w, half_h - 32)
    backSurf = font.render('Back', 1, color.BLUE)
    backRect = backSurf.get_rect()
    backRect.center = (half_w, half_h + 32)
    while True:
        # event
        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if backRect.collidepoint(event.pos):
                    print('click on back')
                    return WELCOME
        # ui
        surface.fill(color.MAINCOLOR)
        surface.blit(titleSurf, titleRect)
        surface.blit(backSurf, backRect)
        pygame.display.update()
        clock.tick(FPS)
