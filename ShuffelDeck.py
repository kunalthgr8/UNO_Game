# Shuffling a list of items passed into it
# Parameters :- Deck list
# Returning :- Deck list

import random 

def shuffelDeck(uno_deck):
    n = len(uno_deck)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        uno_deck[i], uno_deck[j] = uno_deck[j], uno_deck[i]

    return uno_deck
