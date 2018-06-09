#!/usr/bin/env python3

import pygame, sys
from pygame.locals import *

soundObj = pygame.mixer.Sound('../res/beep1.ogg')
soundObj.play()
import time
time.sleep(1)
soundObj.stop()
