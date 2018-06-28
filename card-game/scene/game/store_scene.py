
import pygame
from pygame.locals import *

from gamestate import FPS
import util
from card import card_generator, card_inflater
import color

def show(surface, fpsclock, data):
    print('showing store_scene')

    cardModels = generateCardModels(surface, data)

    while True:
        # mouse or keyboard event
        util.checkForQuit()
        eventDealer(cardModels)
        # render
        surface.fill(color.WHITE)
        x0 = 0
        for cardView, cardRect, _ in cardModels:
            surface.blit(cardView, cardRect)

        pygame.display.update()
        fpsclock.tick(FPS)


def generateCardModels(surface, data):
    w = surface.get_width()
    h = surface.get_height()

    quality = data.map.selected_item.level
    cards = card_generator.gen_store_card(data.current_user_card_pool,
                                          data.card_pool,
                                          quality)

    print('generate cards %s' % cards)

    cardModels = []
    cardWidth = 80
    cardHeight = 100
    rect = Rect(0, 0, cardWidth, cardHeight)
    h0 = int(h - cardHeight / 2 - 20)
    x0 = 0
    for card in cards:
        cardSurf = card_inflater.card_view(card, rect)
        cardRect = cardSurf.get_rect()
        x0 += cardWidth + 10
        cardRect.center = (x0, h0)
        cardModels.append((cardSurf, cardRect, Rect(cardRect))) # the third one for reset

    return cardModels

def eventDealer(cardModels):
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            for i in range(len(cardModels)):
                model = cardModels[i]
                surf, rect, defaultRect = model
                if rect.collidepoint(event.pos):
                    rect.top = defaultRect.top - 20
                else:
                    rect.top = defaultRect.top

                cardModels[i] = (surf, rect, defaultRect)
