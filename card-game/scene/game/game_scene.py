
import pygame
from pygame.locals import *

from scene.game import charector_select_scene, map_scene, store_scene
from record import *

T_EVENT = map_scene.T_EVENT
T_STORE = map_scene.T_STORE
T_BATTLE = map_scene.T_BATTLE

def runGame(surface, fpsclock, data) :
    if not hasattr(data.user, 'init') :
        charector_select_scene.show(surface, fpsclock, data)

    w = surface.get_width()
    h = surface.get_height()
    dRect = Rect(0, 0, int(w/2), int(h/2))
    dRect.center = (int(w/2), int(h/2))

    record(data)
    record(data.user)

    while True:
        status = map_scene.show(surface, fpsclock, data)
        if status is map_scene.SELECT_FINISH :
            s = data.map.selected_item
            if s is None:
                # game may be over but how could it be?
                break

            assert (s.type in [T_EVENT, T_STORE, T_BATTLE]), "unexpected map_item type meet: %s" % s.type
            if s.type == T_EVENT:
                nop = 1
            elif s.type == T_STORE:
                store_scene.show(surface, fpsclock, data)
            elif s.type == T_BATTLE:
                nop = 1
        elif status is map_scene.DONE:
            print('game is over~')
            return

        if s and s.type == T_STORE:
            data.map.current_item = data.map.selected_item

    print("game_scene is done\n")
