
import pygame
from pygame.locals import *

import color
from view import view

def card_view(card, rect):
    w = rect.width
    h = rect.height
    midW = int(w / 2)
    midH = int(h / 2)

    mainSurf = pygame.Surface((w, h))
    mainSurf.fill(color.YELLOW)
    font = pygame.font.Font('freesansbold.ttf', 16)
    titleSurf = font.render(card.name, 1, color.BLACK)
    content = ""
    for func in card.functional:
        content += "deal %d %s to %s," % (func.power, func.func, func.target)
    contentSurf = view.TextView(content, 8, int(w * 0.8), int(w * 0.4))
    image_path = card.imagef
    if image_path is None:
        image_path = 'res/battle-darker.png'
    imageSurf = pygame.image.load(image_path)
    imageWidth = int(w * 0.8)
    imageHeight = int(h * 0.4)
    imageSurf = pygame.transform.scale(imageSurf, (imageWidth, imageHeight))
    imageRect = imageSurf.get_rect()
    imageRect.center = (midW, int(h * 0.25))
    mainSurf.blit(imageSurf, imageRect)
    titleRect = titleSurf.get_rect()
    titleRect.center = (midW, int(h * 0.5))
    mainSurf.blit(titleSurf, titleRect)
    contentRect = contentSurf.get_rect()
    contentRect.center = (midW, int(h * 0.6))
    mainSurf.blit(contentSurf, contentRect)

    return mainSurf
    
