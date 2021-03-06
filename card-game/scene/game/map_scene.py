
import pygame
from pygame.locals import *

from gamestate import *
from util import *
import color
from res import resParser

T_EVENT = map_item.T_EVENT
T_STORE = map_item.T_STORE
T_BATTLE = map_item.T_BATTLE

LIGHTDICT = {T_STORE: pygame.image.load(resParser.getPath('store-lighter.png')),
             T_EVENT: pygame.image.load(resParser.getPath('event-lighter.png')),
             T_BATTLE: pygame.image.load(resParser.getPath('battle-lighter.png'))}

DARKDICT = {T_STORE: pygame.image.load(resParser.getPath('store-darker.png')),
            T_EVENT: pygame.image.load(resParser.getPath('event-darker.png')),
            T_BATTLE: pygame.image.load(resParser.getPath('battle-darker.png'))}

ICONSIZE = 40

SELECT_FINISH = 'select_finish'
DONE = 'done'

def show(surface, fpsclock, data):
    print('map_scene is showing')

    # scan: see how many layer
    map = data.map
    li = map.current_item.next
    if len(li) <= 0 :
        return DONE
    if map.selected_item == map.current_item:
        map.selected_item = None
    if map.selected_item is None:
        map.selected_item = li[0]

    while True:
        # event stuff
        checkForQuit()

        status = event_dealer(map)
        if status == SELECT_FINISH:
            return SELECT_FINISH

        # draw it
        surface.fill(color.WHITE)

        result = draw_map(surface, data.map)
        if result is DONE:
            # game is over ?
            return DONE

        pygame.display.update()
        fpsclock.tick(FPS)

def event_dealer(map):
    LEFT = 'left'
    RIGHT = 'right'
    move = None
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in (K_LEFT, K_a):
                move = LEFT
            elif event.key in (K_RIGHT, K_d):
                move = RIGHT
            elif event.key is K_RETURN:
                return SELECT_FINISH

        elif event.type in [MOUSEMOTION, MOUSEBUTTONDOWN]:
            _list = map.current_item.next
            if _list:
                rect = Rect(0, 0, ICONSIZE, ICONSIZE)
                for item in _list:
                    rect.center = item.point

                    if rect.collidepoint(event.pos):
                        map.selected_item = item

                        print('%s' % (event.type))

                        if event.type == MOUSEBUTTONDOWN:
                            return SELECT_FINISH

    if move:
        li = map.current_item.next
        _i = li.index(map.selected_item)
        size = len(li)
        if move is LEFT:
            index = _i - 1
            if index < 0:
                index = 0
            map.selected_item = li[index]
        elif move is RIGHT:
            index = _i + 1
            if index >= size:
                index = size - 1
            map.selected_item = li[index]


def draw_map(surface, map):
    header = map.header
    current_item = map.current_item
    selected_item = map.selected_item

    if not selected_item or selected_item not in current_item.next:
        if not len(current_item.next) :
            return DONE
        selected_item = current_item.next[0]

    def g(item):
        return get_proper_image(item, current_item, selected_item)

    items = [header]
    count = 0
    maxCount = 100
    history = [] # The drawn items live here
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
            if list_contain(history, item):
                continue
            history.append(item)
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


map_scene_blink = False
map_scene_blink_count = 0
map_scene_blink_count_max = 5
def get_proper_image(map_item, current_item, selected_item):
    global map_scene_blink, map_scene_blink_count

    dictionary = LIGHTDICT
    if map_item.selected :
        dictionary = DARKDICT

    if current_item in map_item.prev :
        dictionary = LIGHTDICT

    if map_item is selected_item:
        if map_scene_blink:
            dictionary = DARKDICT
        else:
            dictionary = LIGHTDICT

        map_scene_blink_count += 1
        if map_scene_blink_count > map_scene_blink_count_max:
            map_scene_blink = not map_scene_blink
            map_scene_blink_count = 0

    return dictionary[map_item.type]
