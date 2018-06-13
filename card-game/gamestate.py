#!/usr/bin/env python3

WELCOME='welcome'
CONFIG='config'
CHARACTER='charecter'
MAP='map'
GAME='game'
EXIT='exit'

FPS=30

class man :
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
