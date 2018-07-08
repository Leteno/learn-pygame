import pygame
from pygame.locals import *

from runnable.elapsingtool import ElapsingTool
from widget.view.TextView import TextView

class PrintWord:
    STANDARD_W = 200
    STANDARD_H = 120
    TEXTWIDTH = int(STANDARD_W * 0.7)
    dialogBG = pygame.image.load('res/speaking-dialog.png')
    def __init__(self, words, interval, after=0, width=STANDARD_W, height=STANDARD_H, point=(0,100)):
        self.words = words
        self.width = self.STANDARD_W
        self.height = self.STANDARD_H
        self.point = point
        self.lastText = ''
        self.lastSurf = None
        self.elapsing = ElapsingTool(interval, after=after)

    def kick(self):
        self.elapsing.kick()

    def getElapsingTool(self):
        return self.elapsing

    def show(self, canvas):
        self.kick()
        # get TextView
        surf = self.lastSurf
        currentText = self.words[:int(len(self.words) * self.elapsing.percentage())]
        if not self.lastText == currentText:
            self.lastSurf = TextView(currentText, 12, self.TEXTWIDTH)
            self.lastText = currentText
        rect = self.dialogBG.get_rect()
        rect.bottomleft = self.point
        dialogTopLeft = rect.topleft
        canvas.blit(self.dialogBG, rect)
        if self.lastSurf:
            rect = self.lastSurf.get_rect()
            rect.topleft = (30 + dialogTopLeft[0], 30 + dialogTopLeft[1])
            canvas.blit(self.lastSurf, rect)
