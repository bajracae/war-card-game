# War Card Game

The War Card Game project is a terminal based game that is an adaption of the famous card game, War. This project is the programming assignment portion for one of my job applications.

---

## How to Play War (Game Rules)

- This is a two player game. The main objective of the game is to collect all the cards.
- The game starts with a shuffled deck of cards with the jokers removed meaning there are 52 cards in the game deck.
- After shuffling the deck, deal out the cards to each player (1 for p1, 1 for p2... etc).
- Each player draws a card from their deck and displays it simultaneously. The player with the highest ranking card wins the pile.
  - Rank goes as follows (high to low): A, K, Q, J... 4, 3, 2, 1.
- The winning player puts the won cards at the bottom of their deck.
- When both players draw the same value card, they go to "war".
- Each player draws 3 cards face down and displays the 4th card. The player with the highest ranking card wins the pile.
- If both players draw the same value card again after the first war, they draw 3 cards each again and display the 4th card. This continues until one of the players win.
- If a player does not have enough cards to use for "war", they lose the game.
- If both players run out of cards before the "war" ends, then the game ends in a tie.

---

## Setup (Prerequisites)

Install Python 3 and (preferably) Git Bash into your local computer

---

## How to Run the Game

The following steps show how to run the War Card Game on a computer.

- Clone the repository
- Open the repository in a terminal
- Using pip, install the libraries listed in requirements.txt
  - [Optional] Create a Python virtual environment to manage the installation of all the libraries. More information on this step can be found here: <https://docs.python.org/3/library/venv.html>
  - Run ```pip install -r requirements.txt``` to install the libraries. If you come across an error, try adding a `--user` flag after "pip install"
- Run main.py using ```python main.py```

---

## Controls

The controls are very simple. All you need to do is press "ENTER" to flip the top card from your deck and "q" if you want to quit the game.

---

## Conclusion

### Assumptions/Edge Cases

The objective for this assignment was to implement "War". However, the instructions on how to implement it and what it should look like were open-ended. With that being the case, I made the assumption that I have a lot of freedom on how to go about achieving the objective. To simplify the process, I decided to make this game a terminal based since I have experience with that in the past. I did not want to spend the short amount of time trying to learn how to use one of Python's game development libraries.

During my research process, I came different ways to play War. As a result, I created a list of assumptions about the rules of the game.

- Assumption 1:
  - During "war", each player draws 3 cards face down and uses the 4th card as the "battle" card. The player with the highest ranking card wins the pile.
  - Some tutorials says that each player has to only draw 1 card face down and the 2nd card serves as the "battle" card. I deterred from this rule because it appeared in a small number of tutorials.

- Assumption 2:
  - If a player does not have enough cards to use for "war", they lose the game.
  - There were tutorials that said the player can use the last card they have as the "battle" card but because this rule was uncommon, I did not apply to my game. This rule would also extend the duration of games so I did not implement it to avoid that.

- Assumption 3/Edge Case:
  - If both players run out of cards before the "war" ends, then the game ends in a tie.
  - Some variations of the allow players to use their last card as their "battle" card during a war. This means the only way a game ends in a tie is if both players run out of cards at the same time after multiple rounds of war. Since I already set the rule that any player that does not have enough cards for "war" loses, I decided to make the game fair and set the rules that if both players do not have enough then they both "lose".
  - There is a low chance that the players will go into continuous series of wars and end up not having enough cards in the last round. To cover this edge case, I set the assumption to end the game in a tie.

- Assumption 4:
  - Discard Joker cards from the deck of cards.
  - I decided to discard the Joker cards because most tutorials of the game do not include them.

### Edge Cases (continued)

War is a simple game so there were only a fewedge cases to keep in mind during my planning and implementation stages.

- Edge case 1:
  - If a player goes into a "war" but has less than 4 cards (3 for face down and 1 for battle) in their hand, then end the game with the other player as a winner.

### If Given More Time

My current implementation is terminal based but if I was given more time, I would have used a Python game development library like PyGame to implement this game with a GUI. During my planning process, I had wanted to build an interactive game using something like PyGame but due to its complexity and my limited time, I decided to simplify and build a terminal based game instead.

I would have also used automated testing methods on my game to verify that it runs smoothly and the user inputs are error handled.
