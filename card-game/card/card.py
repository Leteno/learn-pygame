
import json, os
from res import resParser

T_ENEMY = 'enemy'
T_FRIEND = 'friend'

F_DAMAGE = 'damage'
F_HEAL = 'heal'
F_STAT = 'stat'

class card_func :
    def __init__(self):
        self.target = T_ENEMY
        self.func = F_DAMAGE
        self.power = 1

    def __str__(self):
        return 'target: %s, func: %s, power: %d' % (self.target, self.func, self.power)

class card :
    def __init__(self):
        self.name = "undefine"
        self.level = 1
        self.cost = 1
        self.imagef = resParser.getPath('card-001.png')
        self.functional = []

    def __str__(self):
        return 'name: %s, level: %d, cost: %d, functional: %s' % (self.name, self.level, self.cost, self.functional)

class game_card_pool:
    def __init__(self):
        # store id in common_card_pool
        self.user_card_pool = []
        self.monster_card_pool = []
        self.store_card_pool = []
        # store {'id': card}
        self.all_card_pool = {}

    def __str__(self):
        return ('user_card_pool %s' % (self.user_card_pool)) + ('monster_card_pool %s' % self.monster_card_pool) + ('store_card_pool %s' % self.store_card_pool) + ('all_card_pool %s' % self.all_card_pool)

# card group
USER_CG = 'user'
MONS_CG = 'monster'
STOR_CG = 'store'

def get_card_pool(filename):
    assert os.path.exists(filename), 'Cannot find card file: %s' % filename
    card_file = open(filename, 'r')
    card_datas = json.load(card_file)
    card_file.close()
    pool = game_card_pool()
    user_pool = pool.user_card_pool
    monster_pool = pool.monster_card_pool
    store_pool = pool.store_card_pool
    dict_pool = pool.all_card_pool

    for d in card_datas :
        card = get_card(d)
        id = card.id
        dict_pool[id] = card
        if hasattr(d, 'group') :
            if USER_CG in d['group']:
                user_pool.append(id)
            if MONS_CG in d['group']:
                monster_pool.append(id)
            if STORE_CG in d['group']:
                store_pool.append(id)
        else:
            user_pool.append(id)
            monster_pool.append(id)
            store_pool.append(id)

    return pool


def get_card(data):
    c = card()
    c.id = data['id']
    c.name = data['name']
    c.level = data['level']
    c.cost = data['cost']
    for fun in data['functional']:
        cfunc = card_func()
        cfunc.target = fun['target']
        cfunc.func = fun['func']
        cfunc.power = fun['power']
        c.functional.append(cfunc)
    return c
    
