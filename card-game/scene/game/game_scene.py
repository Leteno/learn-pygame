
from scene.game import charector_select_scene, map_scene
from record import *

def runGame(surface, fpsclock, data) :
    if not hasattr(data.user, 'init') :
        charector_select_scene.show(surface, fpsclock, data)

    record(data)
    record(data.user)

    while True:
        status = map_scene.show(surface, fpsclock, data)
        if status is map_scene.SELECT_FINISH :
            break
    print("game_scene is done\n")
