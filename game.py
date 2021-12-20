from deck import Deck
from player import Player

from colorama import init
from pyfiglet import Figlet
from termcolor import colored

class Game(object):
    def __init__(self):
        self.run_game()

    def run_game(self):
        self.header()

        deck = Deck()

        player = input("Enter your name: ")

        # Create players of the game
        players = [Player(player), Player("Computadora")]

        # Deal out the cards
        while len(deck.deck) > 0:
            for p in players:
                p.add_card(deck.draw_card())

        # Draw one card from each player's pile
        while True:
            # Player 1, Player 2 fields
            field = [[], []]

            print("====")
            print("{}: {} cards".format(player, players[0].num_cards()))
            print("{}: {} cards".format("Computadora", players[1].num_cards()))
            print("====")

            while True:
                field[0].append(players[0].pop_card())
                field[1].append(players[1].pop_card())

                p1_card_rank = field[0][-1].get_rank()
                p2_card_rank = field[1][-1].get_rank()

                if p1_card_rank > p2_card_rank:
                    all_cards = [j for i in field for j in i]
                    players[0].prepend_cards(all_cards)
                    break
                elif p1_card_rank < p2_card_rank:
                    all_cards = [j for i in field for j in i]
                    players[1].prepend_cards(all_cards)
                    break
                else:
                    print("War!")
                    
                    if players[0].num_cards() < 4 and players[1].num_cards() >= 4:
                        print("Player 1 doesn't have enough cards to wage war. Player 2 wins!")
                        exit()

                    elif players[1].num_cards() < 4 and players[0].num_cards() >= 4:
                        print("Player 1 doesn't have enough cards to wage war. Player 1 wins!")
                        exit()

                    elif players[0].num_cards() < 4 and players[1].num_cards() < 4:
                        print("Not enough cards to wage a war. Game has ended in a tie.")
                        exit()

                    else:
                        for c in range(0, 3):
                            field[0].append(players[0].pop_card())
                            field[1].append(players[1].pop_card())
                print("===AFTER Drawing")
                print(players[0].num_cards())
                print(players[1].num_cards())
                print("===")


            if players[0].num_cards() == 0:
                print("Player 2 wins!")
                break

            if players[1].num_cards() == 0:
                print("Player 1 wins!")
                break

            print("Number of " + players[0].name + "'s cards: ", players[0].num_cards())
            print("Number of " + players[1].name + "'s cards: ", players[1].num_cards())
            # exit()


    def header(self):
        init()
        print("*******************************************************************")
        f = Figlet(font='standard')
        print(colored(f.renderText("Let's Play War!"), "red"), end="")
        print("*******************************************************************")
        print("Welcome to an implementation of War, a two-player card game that")
        print("you can be played to help past the time. Please read the README.md")
        print("to learn how to play.")
        print("*******************************************************************")
