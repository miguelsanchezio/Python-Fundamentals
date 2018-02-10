from random import random

def coin_flip():
    r = random()
    if r > 0.5:
        return 'Heads'
    else:
        return 'Tails'

print(coin_flip())
