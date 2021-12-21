import random

from collections import deque
from deck import Deck

class Player(Deck):
    def __init__(self, name):
        self.name = name
        self.cards = deque()

    def get_name(self):
        return self.name

    def add_card(self, card):
        self.cards.append(card)
        return self

    def pop_card(self):
        return self.cards.pop()

    def prepend_cards(self, winnings):
        random.shuffle(winnings)
        for c in winnings:
            self.cards.appendleft(c)

    def show_cards(self):
        for c in self.cards:
            c.show()

    def num_cards(self):
        return len(self.cards)  
