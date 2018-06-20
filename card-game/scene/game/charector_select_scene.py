
import pygame
from pygame.locals import *

from gamestate import FPS
from util import *
import color

def show(surface, clock, data):
    print('showing charector select scene')
    w = surface.get_width()
    h = surface.get_height()
    half_w = int(w / 2)

    font = pygame.font.Font('freesansbold.ttf', 32)
    biggerFont = pygame.font.Font('freesansbold.ttf', 48)
    titleSurf = font.render('Charector select', 1, color.YELLOW)
    titleRect = titleSurf.get_rect()
    okSurf = font.render('OK', 1, color.WHITE)
    okRect = okSurf.get_rect()
    okSurfHover = font.render('OK', 1, color.YELLOW)
    titleRect.center = (half_w, int(titleRect.height / 2) + 10)
    okRect.center = (w - int(okRect.width / 2) - 20, h - int(okRect.height / 2) - 10)
    okButton = okSurf

    minusLabel = biggerFont.render('-', 1, color.WHITE)
    minusRect = minusLabel.get_rect()
    plusLabel = biggerFont.render('+', 1, color.WHITE)
    plusRect = plusLabel.get_rect()

    label_h = minusRect.height + 20
    start = (0, 100)
    array = [[(start[0], start[1]), font.render('Str', 1, color.WHITE), 8,],
             [(start[0], start[1] + label_h), font.render('Dex', 1, color.WHITE), 8,],
             [(start[0], start[1] + label_h * 2), font.render('Int', 1, color.WHITE), 8,]]

    labelSurfIndex = 1
    numIndex = 2

    remain = 0
    for a in array :
        num = a[numIndex]
        a.append(get_num_surface(font, num))

    numSurfIndex = numIndex + 1

    leftLabel = biggerFont.render('left: ', 1, color.YELLOW)
    leftRect = leftLabel.get_rect()
    leftRect.right = w -  100;
    leftRect.centery = start[1]
    leftNumLabel = get_num_surface(font, remain);
    leftNumRect = leftNumLabel.get_rect()
    leftNumRect.right = w - 20;
    leftNumRect.centery = start[1]

    labelRectIndex = numSurfIndex + 1
    minusRectIndex = numSurfIndex + 2
    numRectIndex = numSurfIndex + 3
    plusRectIndex = numSurfIndex + 4
    
    for a in array :
        startX, startY = a[0][0], a[0][1]
        label = a[labelSurfIndex]
        lrect = label.get_rect()
        lrect.left, lrect.centery = startX, startY
        a.append(Rect(lrect))
        startX = startX + 70
        minusRect.left, minusRect.centery = startX, startY
        a.append(Rect(minusRect))
        startX = startX + minusRect.width + 20
        numsurf = a[numSurfIndex]
        numrect = numsurf.get_rect()
        numrect.left, numrect.centery = startX, startY
        a.append(Rect(numrect))
        startX = startX + numrect.width + 20
        plusRect.left, plusRect.centery = startX, startY
        a.append(Rect(plusRect))

    while True :
        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if okRect.collidepoint(event.pos):
                    print('click on ok btn')
                    data.user.str = array[0][numIndex]
                    data.user.dex = array[1][numIndex]
                    data.user.int = array[2][numIndex]
                    data.user.init = True
                    return

            elif event.type == MOUSEBUTTONDOWN:
                for a in array:
                    if a[minusRectIndex].collidepoint(event.pos) and a[numIndex] > 0:
                        a[numIndex] -= 1
                        remain += 1
                        a[numSurfIndex] = get_num_surface(font, a[numIndex])
                        leftNumLabel = get_num_surface(font, remain)
                    elif a[plusRectIndex].collidepoint(event.pos) and remain > 0:
                        a[numIndex] += 1
                        remain -= 1
                        a[numSurfIndex] = get_num_surface(font, a[numIndex])
                        leftNumLabel = get_num_surface(font, remain)

            elif event.type == MOUSEMOTION:
                if okRect.collidepoint(event.pos):
                    okButton = okSurfHover
                else :
                    okButton = okSurf

        surface.fill(color.MAINCOLOR)
        surface.blit(titleSurf, titleRect)
        surface.blit(okButton, okRect)
        surface.blit(leftLabel, leftRect)
        surface.blit(leftNumLabel, leftNumRect)

        for a in array :
            surface.blit(a[labelSurfIndex], a[labelRectIndex])
            surface.blit(minusLabel, a[minusRectIndex])
            surface.blit(a[numSurfIndex], a[numRectIndex])
            surface.blit(plusLabel, a[plusRectIndex])
        
        pygame.display.update()
        clock.tick(FPS)


def get_num_surface(font, num):
    s = '' + str(num)
    if num < 9 :
        s = ' ' + str(num)
    return font.render(s, 1, color.WHITE)
    

