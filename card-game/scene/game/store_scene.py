
import pygame
from pygame.locals import *

from gamestate import FPS
import util
from card import card_generator, card_inflater
import color

from runnable import sequence
from runnable.sequence import Moving
from runnable.task import Task
from widget.Sprite import Sprite
from widget.Vango import Vango
from widget.view.PrintWord import PrintWord
from widget.view.ImageView import ImageView

DEALING = 'DEALING'
SELECTED = 'SELECTED'

class CardModel:
   def __init__(self, surf, rect, defaultRect, selecting, card):
        self.surf = surf
        self.rect = rect
        self.defaultRect = defaultRect
        self.selecting = selecting
        self.card = card

def show(surface, fpsclock, data):
    print('showing store_scene')

    halfW = surface.get_width() / 2
    halfH = surface.get_height() / 2

    cardModels = generateCardModels(surface, data)

    background = pygame.image.load('res/store-background.png')
    storeTable = pygame.image.load('res/store-table.png')
    bossSpeaking = pygame.image.load('res/store-boss-speaking.png')
    boss = Sprite(ImageView(pygame.image.load('res/store-boss-normal.png')))
    printword = Sprite(PrintWord('Hello world, My name is Mr.Zheng', 2000, after=500), position=(200, 160))
    vango = Vango()
    vango.add(boss)
    vango.add(printword)

    task = Task()
    bossMoving = Moving(boss, (halfW-100, halfH), (halfW, halfH), 1000)
    task.put('boss', bossMoving)

    printword.hide()
    def startPrintWords():
       printword.show()
    task.onAfterFinishCallback = startPrintWords

    firstTime = True

    while True:
        # mouse or keyboard event
        util.checkForQuit()
        code, other = eventDealer(cardModels)
        if code == SELECTED:
            _card = other
            print('store_scene select done: %s' % _card)
            data.current_user_card_pool.append(_card)
            return

        # render background
        surface.blit(background, background.get_rect())

        # render boss
        task.process()

        vango.show(surface)

        surface.blit(storeTable, storeTable.get_rect())

        x0 = 0
        for _model in cardModels:
            rect, defaultRect, selecting = _model.rect, _model.defaultRect, _model.selecting
            rect.top = defaultRect.top
            if _model.selecting :
                rect.top -= 20
            surface.blit(_model.surf, _model.rect)

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
        selecting = False
        cardModels.append(CardModel(cardSurf, cardRect, Rect(cardRect), selecting, card)) # the third one for reset

    return cardModels


def eventDealer(cardModels):
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            for _model in cardModels:
                rect = _model.rect
                defaultRect = _model.defaultRect
                if rect.collidepoint(event.pos):
                    _model.selecting = True
                else:
                    _model.selecting = False

        elif event.type == MOUSEBUTTONDOWN:
            for _model in cardModels:
                if _model.selecting :
                    return SELECTED, _model.card

        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                for _model in cardModels:
                    if _model.selecting :
                        return SELECTED, _model.card

            elif event.key in [K_a, K_LEFT]:
                _len = len(cardModels)
                for i in reversed(range(_len)):
                    _model = cardModels[i]
                    if _model.selecting or i == 0:
                        _model.selecting = False
                        _next = cardModels[(i + _len - 1) % _len]
                        _next.selecting = True
                        break
            elif event.key in [K_d, K_RIGHT]:
                _len = len(cardModels)
                for i in range(_len):
                    _model = cardModels[i]
                    if _model.selecting or i == _len - 1:
                        _model.selecting = False
                        _next = cardModels[(i + 1) % _len]
                        _next.selecting = True
                        break


    return DEALING, None
