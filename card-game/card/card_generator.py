
from card import card
import random

def gen_store_card(current_user_card_pool, game_card_pool, quality, size=8):
    result = []
    random.seed()

    result += current_user_card_pool
    random.shuffle(result)
    n = int(size/4)
    result = result[:n]

    ucp_copy = game_card_pool.user_card_pool[:]
    random.shuffle(ucp_copy)
    result += ucp_copy[:size]

    random.shuffle(result)
    real_cards = []
    for id in result[:size]:
        card = game_card_pool.all_card_pool[id]
        real_cards.append(card)

    return real_cards
