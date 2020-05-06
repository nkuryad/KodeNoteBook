
""" @docStart
### Card Game
@docEnd """

# @codeStart

import random

# Concat function combines
# elements of two lists


def concat(x, y):
    i = 0
    n = 0
    z = []
    while i < len(x):
        z.append(x[i])
        i += 1
    while n < len(y):
        z.append(y[n])
        n += 1
    return z


# Join each element of
# first list to every
# element of second list
# ex:- ['a', 'b'] x ['1', '2']
# = ['a1', 'a2', 'b1', 'b2']


def crossJoin(x, y):
    i = 0
    z = []
    while i < len(x):
        n = 0
        while n < len(y):
            z.append(x[i]+y[n])
            n += 1
        i += 1
    return z

# deckCard generates a list of deck cards


def deckCard():
    c = concat(["ace", "king", "queen", "jack"], [
               "2", "3", "4",
               "5", "6", "7",
               "8", "9", "10"])
    res = crossJoin([
        "heart-♥-",
        "spade-♠-",
        "diamond-♦-",
        "club-♣-"], c)
    return res

# shuffle function shuffles the cards

def shuffle(x):
    i = 0
    while i < len(x):
        c = random.randint(0, len(x)-1)
        d = x[i]
        x[i] = x[c]
        x[c] = d
        i += 1
    return x

# Azma luck azma

def gambling(x, y):
    c = random.randint(0, len(x)-1)
    if(y in x[c]):
        return "u won"
    else:
        return "u loose"

# gives the probability by matching given cards in list
def probability(x, y):
    z = 0
    n = 0
    while n < len(x):
        i = 0
        while i < len(y):
            if(y[i] in x[n]):
                z += 1
                break
            i += 1
        n += 1
    return z


print('deckCard-start')
de = deckCard()
print(de)
print('deckCard-end')
print('shuffle-start')
shuffle(de)
print(de)
print('shuffle-end')
print('gambling-start')
print(gambling(de, 'heart'))
print(gambling(de, 'king'))
print(gambling(de, 'ace'))
print('gambling-end')
print('probability-start')
print(probability(de, ['heart', 'brick']))
print(probability(de, ['king', 'jack']))
print('probability-end')


# @codeEnd
