import time

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

        # Name of the players
        computer = "Computadora"
        player = self.get_player_name_from_user()

        # List of Player objects each representing a player
        players = [Player(computer), Player(player)]

        deck = Deck()

        # Deal out the cards to each player
        while len(deck.deck) > 0:
            for p in players:
                p.add_card(deck.draw_card())

        print("\n")
        print("Dealing out cards...")
        print("\n")

        time.sleep(1)

        self.scoreboard(players)

        # Draw one card from each player's pile
        while True:
            # Lists to store Player 1's and 2's played cards in a round
            field = [[], []]

            _ = self.get_game_input_from_user()
            
            # Flag sets to True when war takes place
            in_war = False

            while True:
                field[0].append(players[0].pop_card())
                field[1].append(players[1].pop_card())

                p1_card_rank = field[0][-1].get_rank()
                p2_card_rank = field[1][-1].get_rank()

                # Print different ascii arts based the status of the in_war flag
                if in_war == True:
                    print("*******************************************************************")
                    print("{}'s card".format(colored(players[0].get_name(), "red")))
                    field[0][-1].ascii_card_three_face_down()
                    print("*******************")
                    print("{}'s card".format(colored(players[1].get_name(), "green")))
                    field[1][-1].ascii_card_three_face_down()
                else:
                    print("*******************************************************************")
                    print("{}'s card".format(colored(players[0].get_name(), "red")))
                    field[0][-1].ascii_card()
                    print("*******************")
                    print("{}'s card".format(colored(players[1].get_name(), "green")))
                    field[1][-1].ascii_card()

                # Check players' card ranks and place won cards into the bottom of the winner's deck, activate war if ranks are equal
                if p1_card_rank > p2_card_rank:
                    all_cards = [j for i in field for j in i]
                    players[0].prepend_cards(all_cards)
                    in_war = False
                    print("{} won this round! (╥_╥)".format(colored(players[0].get_name(), "red")))
                    break
                elif p1_card_rank < p2_card_rank:
                    all_cards = [j for i in field for j in i]
                    players[1].prepend_cards(all_cards)
                    in_war = False
                    print("{} won this round! (^__^)".format(colored(players[1].get_name(), "green")))
                    break
                else:
                    print("*******************************************************************")
                    print("WAR!")
                    in_war = True
                    
                    # Check if both players have enough cards to engage in war, each player needed at least 4 cards
                    if players[0].num_cards() < 4 and players[1].num_cards() >= 4:
                        print("{} doesn't have enough cards to wage war. {} wins!".format(colored(players[0].get_name(), "red"), colored(players[1].get_name(), "green")))
                        exit()
                    elif players[1].num_cards() < 4 and players[0].num_cards() >= 4:
                        print("{} doesn't have enough cards to wage war. {} wins!".format(colored(players[1].get_name(), "green"), colored(players[0].get_name(), "red")))
                        exit()
                    else:
                        print("Placing three cards down and flipping the fourth card...")
                        time.sleep(1)
                        for c in range(0, 3):
                            field[0].append(players[0].pop_card())
                            field[1].append(players[1].pop_card())

            # If one player runs out of cards, the other player wins
            if players[0].num_cards() == 0:
                print("{} wins!".format(colored(players[1].get_name(), "green")))
                break
            
            if players[1].num_cards() == 0:
                print("{} wins!".format(colored(players[0].get_name(), "red")))
                break

            print("\n")
            self.scoreboard(players)

    def header(self):
        init()
        print("*******************************************************************")
        f = Figlet(font='standard')
        print(colored(f.renderText("Let's Play War!"), "red"), end="")
        print("*******************************************************************")
        print("Welcome to an implementation of War, a two-player card game that")
        print("you can play pass the time. Please read the README.md to learn")
        print("how to play the game.")
        print("*******************************************************************")

    def scoreboard(self, players):
        print("*******************************************************************")
        print(colored("[ SCOREBOARD ]", "yellow"))
        print(colored("{}: {} cards".format(players[0].get_name(), players[0].num_cards()), "red") + " | " + colored("{}: {} cards".format(players[1].get_name(), players[1].num_cards()), "green")) 
        print("*******************************************************************")

    def get_player_name_from_user(self):
        name = input("Please enter your first name: ")

        while name == "":
            name = input("Invalid input found. Please enter your first name: ")

        return name
    
    def get_game_input_from_user(self):
        user_input = input("Press 'ENTER' to play your next card / 'q' to quit the game: ")

        while user_input != "":
            if user_input == "q":
                print("Quitting the game...")
                time.sleep(0.5)
                exit()
            user_input = input("Invalid input found. Please try again: ")
        
        return user_input
