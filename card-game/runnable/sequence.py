from gamestate import FPS
from datetime import datetime

import pygame
from pygame.locals import *

from widget.view.TextView import TextView
from runnable.elapsingtool import ElapsingTool

class Sequence:
#   def process(self)
#   def getElapsingTool(self)
    pass

class Moving(Sequence):
    def __init__(self, sprite, fromP, toP, interval, after=0):
        """
        surf:  sprite
        fromP: from Point
        toP:   to Point
        """
        self.sprite = sprite
        self.sprite.position = fromP
        self.fromP = fromP
        self.toP = toP
        self.elapsingTool = ElapsingTool(interval, after, lambda x: x * x)

    def process(self):
        """
        canvas: pygame.Surface
        """
        self.elapsingTool.kick()
        positionX = self.fromP[0] - (self.fromP[0] - self.toP[0]) * self.elapsingTool.percentage()
        positionY = self.fromP[1] - (self.fromP[1] - self.toP[1]) * self.elapsingTool.percentage()
        self.sprite.position = (positionX, positionY)

    def getElapsingTool(self):
        return self.elapsingTool

class Delay(Sequence):
    def __init__(self, time):
        self.elapsingTool = ElapsingTool(time)

    def process(self):
        self.elapsingTool.kick()

    def getElapsingTool(self):
        return self.elapsingTool
