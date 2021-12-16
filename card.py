class Card(object):
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def get_rank(self):
        return self.rank

    def show(self):
        print(self.value + " of " + self.suit)