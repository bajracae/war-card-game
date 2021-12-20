class Card(object):
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def get_rank(self):
        return self.rank

    def show(self):
        print(self.value + " of " + self.suit)

    def ascii_card(self):
        print("┌───────┐")
        print("| {:<2}    |".format(self.value))
        print("|       |")
        print("|   {}   |".format(self.suit[0]))
        print("|       |")
        print("|    {:>2} |".format(self.value))
        print("└───────┘") 

    def ascii_card_three_face_down(self):
        print("┌───────┐")
        print("|┌───────┐")
        print("||┌───────┐")
        print("|||┌───────┐")
        print("|||| {:<2}    |".format(self.value))
        print("||||       |")
        print("└|||   {}   |".format(self.suit[0])) 
        print(" └||       |")
        print("  └|    {:>2} |".format(self.value))
        print("   └───────┘")