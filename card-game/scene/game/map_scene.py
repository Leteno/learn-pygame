
import pygame
from pygame.locals import *

from gamestate import *
from util import *
import color

T_EVENT = map_item.T_EVENT
T_STORE = map_item.T_STORE
T_BATTLE = map_item.T_BATTLE

LIGHTDICT = {T_STORE: pygame.image.load('res/store-lighter.png'),
             T_EVENT: pygame.image.load('res/event-lighter.png'),
             T_BATTLE: pygame.image.load('res/battle-lighter.png')}

DARKDICT = {T_STORE: pygame.image.load('res/store-darker.png'),
            T_EVENT: pygame.image.load('res/event-darker.png'),
            T_BATTLE: pygame.image.load('res/battle-darker.png')}


def show(surface, fpsclock, data):
    print('map_scene is showing')

    # scan: see how many layer
    w = surface.get_width()
    h = surface.get_height()
    iconsize = 40
    while True:
        # event stuff
        checkForQuit()

        # draw it
        surface.fill(color.DARKGRAY)

        draw_map(surface, data.map)

        pygame.display.update()
        fpsclock.tick(FPS)

def draw_map(surface, map):
    header = map.header
    current_item = map.current_item
    def g(item):
        return get_proper_image(item, current_item)
    items = [header]
    count = 0
    maxCount = 100
    while items:
        count += 1
        assert count < maxCount, 'count should be less than %d' % maxCount

        next_items = []
        for item in items:
            if item is None:
                continue
            next_items += item.next
            if item.point is None:
                continue
            surf = g(item)
            rect = surf.get_rect()
            rect.center = item.point
            surface.blit(surf, rect)
            if item.prev :
                for i in item.prev:
                    if i is None:
                        continue
                    points = [item.point, i.point]
                    pygame.draw.lines(surface, color.YELLOW, 1, points)

        items = next_items


def get_proper_image(map_item, current_item):
    dictionary = DARKDICT
    if current_item in map_item.prev :
        dictionary = LIGHTDICT
    return dictionary[map_item.type]
