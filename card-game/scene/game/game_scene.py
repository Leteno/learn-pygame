
from scene.game import charector_select_scene
from record import *

def runGame(surface, fpsclock, data) :
    if not hasattr(data.user, 'init') :
        charector_select_scene.show(surface, fpsclock, data)

    record(data)
    record(data.user)
        
    print("game_scene is done\n")
