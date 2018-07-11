
import pygame
from pygame.locals import *

MATCH = 'match'
MISMATCH = 'mismatch'

class Button:
    COMMON = 'common'
    HOVER = 'hover'
    CLICK = 'click'
    def __init__(self, commonSurf, hoverSurf = None, clickSurf = None, onclick = None, position = None):
        self.commonSurf = commonSurf
        self.hoverSurf = hoverSurf
        self.clickSurf = clickSurf
        self.position = position
        self.onclick = onclick
        self.state = self.COMMON

    def setCenterPosition(self, position):
        self.position = position

    def show(self, surf):
        assert self.position, 'position should not be None'
        drawSurf = self.getProperSurf()
        drawRect = drawSurf.get_rect()
        drawRect.center = self.position
        surf.blit(drawSurf, drawRect)

    def getProperSurf(self):
        if self.state == self.HOVER and self.hoverSurf:
            return self.hoverSurf
        if self.state == self.CLICK and self.clickSurf:
            return self.clickSurf
        if self.state == self.CLICK:
            return self.hoverSurf
        return self.commonSurf

    def event(self, event):
        assert self.position, 'position should not be None'
        surf = self.getProperSurf()
        rect = surf.get_rect()
        rect.center = self.position
        print(event)
        if not hasattr(event, 'pos'):
            return MISMATCH
        if not rect.collidepoint(event.pos):
            self.state = self.COMMON
            return MISMATCH

        if event.type == MOUSEMOTION:
            self.state = self.HOVER
        elif event.type in [MOUSEBUTTONDOWN, MOUSEBUTTONUP]:
            self.state = self.CLICK
            if self.onclick:
                self.onclick()
        else:
            self.state = self.COMMON
