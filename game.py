from deck import Deck
from player import Player

class Game(object):
    def __init__(self):
        self.run_game()

    def run_game(self):
        deck = Deck()

        # Create players of the game
        players = [Player("Player 1"), Player("Player 2")]
        # for p in range(1, 3):
        #     players.append(Player("P{}".format(p)))

        # Deal out the cards
        while len(deck.deck) > 0:
            for p in players:
                p.add_card(deck.draw_card())

        # Draw one card from each player's pile
        while True:
            # Player 1, Player 2 fields
            field = [[], []]

            print("====")
            print("Starting")
            print(len(players[0].cards))
            print(len(players[1].cards))
            print("====")

            while True:
                field[0].append(players[0].pop_card())
                field[1].append(players[1].pop_card())

                p1_card_rank = field[0][-1].get_rank()
                p2_card_rank = field[1][-1].get_rank()
                print(len(players[0].cards))
                print(len(players[1].cards))
                print("====")
                print(p1_card_rank)
                print(p2_card_rank)
                print("====")

                if p1_card_rank > p2_card_rank:
                    all_cards = [j for i in field for j in i]
                    players[0].prepend_cards(all_cards)
                    break
                elif p1_card_rank < p2_card_rank:
                    all_cards = [j for i in field for j in i]
                    players[1].prepend_cards(all_cards)
                    break
                else:
                    field[0].append(players[0].pop_card())
                    field[0].append(players[0].pop_card())
                    field[0].append(players[0].pop_card())

                    field[1].append(players[1].pop_card())
                    field[1].append(players[1].pop_card())
                    field[1].append(players[1].pop_card())

            print(len(players[0].cards))
            print(len(players[1].cards))
            exit()


