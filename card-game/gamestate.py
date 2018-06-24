#!/usr/bin/env python3

import copy, re, os

from card import card

WELCOME='welcome'
CONFIG='config'
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

class map_item :
    T_EVENT = 'event'
    T_STORE = 'store'
    T_BATTLE = 'battle'
    def __init__(self, type, level = 1):
        self.type = type
        self.level = level
        self.point = None
        self.next = []
        self.prev = []

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, newtype):
        assert (newtype in [map_item.T_EVENT, map_item.T_STORE, map_item.T_BATTLE]), 'there is an unexpected type of map_item: "%s"' % (newtype)
        self._type = newtype

    def addChild(self, item) :
        item.prev = self
        self.next.append(item)


class map_data :
    def __init__(self):
        self.header = None
        self.current_item = self.header
        self.selected_item = None

    def read_from_file(self, filename):
        assert os.path.exists(filename), 'Cannot find the map file: %s' % (filename)
        mapFile = open(filename, 'r')
        content = mapFile.readlines() + ['\r\n']
        mapFile.close()

        numRe = re.compile('num: *([0-9]+)')
        typeRe = re.compile('type: *(\w+)')
        levelRe = re.compile('level: *([0-9]+)')
        pointRe = re.compile('point: \(([0-9]+), *([0-9]+)\)')
        nextRe = re.compile('next: \(([0-9, ]+)\)')
        _map = {}
        stashLines = []
        for lineNum in range(len(content)):
            line = content[lineNum].lstrip('\r\n')

            if ';' in line:
                line = line[:line.find(';')]

            if line != '':
                stashLines.append(line)
            elif line == '' and len(stashLines) > 0:
                item = map_item(map_item.T_EVENT)
                num = None
                for li in stashLines:
                    tmp = numRe.match(li)
                    if tmp is not None:
                        num = tmp.group(1)
                        continue
                    tmp = typeRe.match(li)
                    if tmp is not None:
                        item.type = tmp.group(1)
                        continue
                    tmp = levelRe.match(li)
                    if tmp is not None:
                        item.level = tmp.group(1)
                        continue
                    tmp = pointRe.match(li)
                    if tmp is not None:
                        item.point = (int(tmp.group(1)), int(tmp.group(2)))
                        continue
                    tmp = nextRe.match(li)
                    if tmp is not None:
                        try:
                            nlist = tmp.group(1)
                            item.next = nlist.split(', ')
                        except Exception as e:
                            print('skip exception at %d, of %s' % (lineNum, e))

                if num is not None:
                    _map[num] = item
                    print('enter new item %s: %s' % (num, item))

                stashLines = []

        for k in _map:
            item = _map[k]
            keyofnexts = item.next
            item.next = []
            for k0 in keyofnexts:
                v0 = _map[k0]
                if v0 is not None:
                    item.next.append(v0)
                    v0.prev.append(item)

        self.header = _map['0'] # please please  "num: 0"
        self.current_item = self.header
        _map.clear()
        

class game_data :
    def __init__(self):
        self.user = charector(charector.PLAYER)
        self.level = 0
        self.score = 0
        self.config = config()
        self.map = map_data()
        self.map.read_from_file('res/map.dat')
        self.card_pool = card.get_card_pool('res/card.dat')
        self.current_user_card_pool = []

    def reset(self):
        delattr(self.user, 'init')
