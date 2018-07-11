
import pygame
from pygame.locals import *

import color
from widget.view.Drawwer import Drawwer

class TextView(Drawwer):
    def __init__(self, string, textsize, width, height=0, textcolor=color.BLACK, bgcolor=color.WHITE):
        self.string = string
        self.textsize = textsize
        self.width = width
        self.height = height
        self.textcolor = textcolor
        self.bgcolor = bgcolor

        self.surf = None

    def onDraw(self, canvas, position):
        surf = self.getSurf()
        rect = surf.get_rect()
        rect.center = position
        canvas.blit(surf, rect)

    def getSurf(self):
        if not self.surf:
            self.surf = self.create_surf()
        return self.surf

    def create_surf(self):
        font = pygame.font.Font('freesansbold.ttf', self.textsize)
        metrics = font.metrics(self.string)

        ww = []
        word = ''
        sumW, maxH = 0, 0
        for metric, ch in zip(metrics, self.string):
            w0, h0 = metric[-2], metric[-1]
            if h0 > maxH:
                maxH = h0

            word += ch
            sumW += w0
            if ch in ' \t\n:[],;\'"':
                ww.append((word, sumW))
                sumW = 0
                word = ''

        if len(word) > 0:
            ww.append((word, sumW))

        line = ''
        currentWidth = 0
        lines = []
        for word, length in ww:
            if currentWidth + length > self.width:
                lines.append(line)
                line = ''
                currentWidth = 0

            line += word
            currentWidth += length

        if len(line) > 0:
            lines.append(line)

        if self.height <= 0:
            self.height = self.textsize * len(lines)

        print('text height: %d' % self.height)

        result = pygame.Surface((self.width, self.height))
        result.fill(self.bgcolor)

        _h = 0
        for line in lines:
            surf = font.render(line, 1, self.textcolor)
            rect = surf.get_rect()
            rect.left = 0
            rect.top = _h
            _h += maxH
            result.blit(surf, rect)
        print(ww)
        return result
