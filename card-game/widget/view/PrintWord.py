import pygame
from pygame.locals import *

from runnable.elapsingtool import ElapsingTool
from widget.view.TextView import TextView
from widget.view.Drawwer import Drawwer

class PrintWord(Drawwer):
    STANDARD_W = 200
    STANDARD_H = 120
    TEXTWIDTH = int(STANDARD_W * 0.7)
    dialogBG = pygame.image.load('res/speaking-dialog.png')
    def __init__(self, words, interval, after=0, width=STANDARD_W, height=STANDARD_H):
        self.words = words
        self.width = self.STANDARD_W
        self.height = self.STANDARD_H
        self.lastText = ''
        self.lastSurf = None
        self.elapsing = ElapsingTool(interval, after=after)

    def kick(self):
        self.elapsing.kick()

    def getElapsingTool(self):
        return self.elapsing

    def onDraw(self, canvas, position):
        self.kick()
        # get TextView
        currentLen = int(len(self.words) * self.elapsing.percentage())
        currentText = self.words[:currentLen]
        if not self.lastText == currentText:
            self.lastSurf = TextView(currentText, 12, self.TEXTWIDTH).getSurf()
            print(self.lastSurf.get_rect())
            self.lastText = currentText
        rect = self.dialogBG.get_rect()
        rect.bottomleft = position
        dialogTopLeft = rect.topleft
        canvas.blit(self.dialogBG, rect)
        if self.lastSurf:
            rect = self.lastSurf.get_rect()
            rect.topleft = (30 + dialogTopLeft[0], 30 + dialogTopLeft[1])
            canvas.blit(self.lastSurf, rect)
