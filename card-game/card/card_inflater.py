
import pygame
from pygame.locals import *

import color
from widget.view.TextView import TextView

_CardBackground = None

class CardBackground:
    surf = None
    width = 0
    height = 0

class Pool:
    pool = {}

    def put(self, card, cardsurf):
        self.pool[card.name] = cardsurf

    def get(self, card, width, height):
        if card.name not in self.pool:
            surf = self.generateCardSurf(card, width, height)
            self.put(card, surf)
        surf = self.pool[card.name]
        rect = surf.get_rect()
        if width != rect.width or height != rect.height:
            surf = pygame.transform.scale(surf, (width, height))
            self.put(card, surf)
        return surf

    def generateCardSurf(self, card, width, height):
        surf = pygame.image.load(card.imagef)
        rect = surf.get_rect()
        if width != rect.width or height != rect.height:
            surf = pygame.transform.scale(surf, (width, height))
        return surf

_pool = Pool()
def getCardSurf(card, width, height):
    return _pool.get(card, width, height)
