
# We are generating a deck of 108 cards of UNO
# Parameters Passes :- Null
# Returning :- Deck List


def builDeck():

    deck = []
    
    colors = ["Red", "Green", "Yellow", "Blue"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
    wilds = ["Wild", "Wild Draw Four"]

    for wild in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])

    for color in colors:
        for value in values:
            cardVal = "{} {}".format(color, value)
            deck.append(cardVal)
            if (value != 0):
                deck.append(cardVal)

    return deck


builDeck()
