#!/usr/bin/env python3

import pygame
from pygame.locals import *

import sys

def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

def list_contain(list, item):
    try:
        return list.index(item) >= 0
    except:
        return False
