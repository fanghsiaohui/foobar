#!/usr/bin/env python
import random, sys
import numpy as np

s = '\u2660'
h = '\u2665'
c = '\u2663'
d = '\u2666'

card = ['A', '2', '3', '4', '5','6', '7',
        '8', '9', '10', 'J', 'Q', 'K']
spadeCards = [i + s for i in card]
heartCards = [i + h for i in card]
clubsCards = [i + c for i in card]
diamondCards = [i + d for i in card]
cards = []
cards.extend(spadeCards)
cards.extend(heartCards)
cards.extend(clubsCards)
cards.extend(diamondCards)

def chooseCards(m=5, cards = cards):
    choiceCards = np.random.choice(cards, m)
    return choiceCards

def flop(m=20, n=3):
    for i in range(m):
        flop = chooseCards(n)
        print("{:2d}: ".format(i+1), end='\t')
        for j in flop:
            print(j, end="\t")
        print()

if __name__ == "__main__":
    try:
        n = sys.argv[1]
        n = int(n)
    except:
        n = 3
    flop(20, n)
