import random

from card import Card


class Deck(object):
    def __init__(self):
        self.deck = []
        self.build()
        self.shuffle()

    def build(self):
        suits = ["clubs", "diamonds", "hearts", "spades"]
        values = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q",
                  13: "K", 14: "A"}

        for s in suits:
            for r, v in values.items():
                card = Card(s, r, v)
                self.deck.append(card)

    def draw_card(self):
        return self.deck.pop()

    def show(self):
        for c in self.deck:
            c.show()

    def shuffle(self):
        return random.shuffle(self.deck)
