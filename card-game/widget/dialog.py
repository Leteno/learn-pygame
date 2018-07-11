
import pygame
from pygame.locals import *

from widget.view.TextView import *
from widget.view.Button import *

from gamestate import FPS

from util import *

import color

class dialog:

    def __init__(self, title, message, button, rect):
        self.title = title
        self.message = message
        self.button = button
        self.rect = rect

    def show(self, surface, fpsclock):
        w = self.rect.width
        h = self.rect.height
        _w = int(w * 0.8)

        _dismiss = False
        def dismiss():
            _dismiss = True

        titleView = TextView(self.title, 24, _w)
        messageView = TextView(self.message, 18, _w)

        buttonViewCommon = TextView(self.button, 20, 100)
        buttonViewHover = TextView(self.button, 20, 100, textcolor=color.WHITE, bgcolor=color.BRIGHTYELLOW)
        buttonCenter = (100, 100)
        button = Button(buttonViewCommon, buttonViewHover, position=buttonCenter, onclick=dismiss)

        titleRect = titleView.get_rect()
        titleRect.center = (int(w / 2), int(titleRect.height / 2) + 10)
        messageRect = messageView.get_rect()
        messageRect.center = (int(w / 2), int(messageRect.height / 2 + h * 0.3))

        while True:
            checkForQuit()
            # event capture

            for event in pygame.event.get():
                button.event(event)

            surface.blit(titleView, titleRect)
            surface.blit(messageView, messageRect)
            button.show(surface)

            pygame.display.update()
            fpsclock.tick(FPS)
