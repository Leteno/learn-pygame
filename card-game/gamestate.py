#!/usr/bin/env python3

WELCOME='welcome'
CONFIG='config'
MAP='map'
GAME='game'
EXIT='exit'

FPS=30

class charector :
    PLAYER = 'player'
    ANIMAL = 'animal'
    def __init__(self, species, str=1, dex=1, int=1, snum=1, dnum=1, inum=1):
        self.str = str
        self.dex = dex
        self.int = int
        self.snum = snum
        self.dnum = dnum
        self.inum = inum
        self.species = species

    def filter_enemy(self, list):
        result = []
        for m in list:
            if not isinstance(m, man):
                continue
            if self.species is not m.species :
                result.append(m)
        return result

    def filter_friend(self, list):
        result = []
        for m in list:
            if not isinstance(m, man):
                continue
            if self.species is m.species :
                result.append(m)
        return result

    def __str__(self):
        return 'class man str: {}, dex: {}, int: {}, snum: {}, dnum: {}, inum: {}, species: {}'.format(
            self.str, self.dex, self.int, self.snum, self.dnum, self.inum, self.species)

class config :
    def __init__(self):
        self.sound = 4
        self.difficulty = 1

class game_data :
    def __init__(self):
        self.user = charector(charector.PLAYER)
        self.level = 0
        self.score = 0
        self.config = config()

    def reset(self):
        delattr(self.user, 'init')
