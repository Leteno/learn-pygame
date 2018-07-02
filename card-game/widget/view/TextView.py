
import pygame
from pygame.locals import *

import color

def TextView(string, textsize, width, height, textcolor=color.BLACK, bgcolor=color.WHITE):
    textView = pygame.Surface((width, height))
    textView.fill(bgcolor)
    font = pygame.font.Font('freesansbold.ttf', textsize)
    metrics = font.metrics(string)

    ww = []
    word = ''
    sumW, maxH = 0, 0
    for metric, ch in zip(metrics, string):
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

    _h = 0
    line = ''
    currentWidth = 0
    for word, length in ww:
        if currentWidth + length > width:
            surf = font.render(line, 1, textcolor)
            rect = surf.get_rect()
            rect.left = 0
            rect.top = _h
            _h += maxH
            textView.blit(surf, rect)

            line = ''
            currentWidth = 0

        line += word
        currentWidth += length

    if len(line) > 0:
        surf = font.render(line, 1, textcolor)
        rect = surf.get_rect()
        rect.left = 0
        rect.top = _h
        _h += maxH
        textView.blit(surf, rect)

    print(ww)

    return textView
