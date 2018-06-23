
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

SELECT_FINISH = 'select_finish'
DONE = 'done'

def show(surface, fpsclock, data):
    print('map_scene is showing')

    # scan: see how many layer
    w = surface.get_width()
    h = surface.get_height()
    iconsize = 40
    while True:
        # event stuff
        checkForQuit()

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

        m = data.map
        li = m.current_item.next
        if len(li) < 0 :
            return DONE
        if m.selected_item is None:
            m.selected_item = li[0]

        sel_i = li.index(m.selected_item)
        size = len(li)
        l_sel_i = sel_i - 1
        if l_sel_i < 0:
            l_sel_i = 0
        r_sel_i = sel_i + 1
        if r_sel_i >= size:
            r_sel_i = size - 1

        if move is LEFT:
            m.selected_item = li[l_sel_i]
        elif move is RIGHT:
            m.selected_item = li[r_sel_i]

        # draw it
        surface.fill(color.WHITE)

        result = draw_map(surface, data.map)
        if result is DONE:
            # game is over ?
            return DONE

        pygame.display.update()
        fpsclock.tick(FPS)


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


map_scene_blink = False
map_scene_blink_count = 0
map_scene_blink_count_max = 5
def get_proper_image(map_item, current_item, selected_item):
    global map_scene_blink, map_scene_blink_count

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
