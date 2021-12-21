# war-card-game
This game is a programming assignment for a job application.

## Download libraries
1) Make a Python virtual environment (optional)
2) Install all the libraries in requirements.txt
   1) ```pip install -r requirements.txt```


## Python version
I used Python 2.7.5 during the development of this project.

DUE DATE OF THIS IS THE 12/22/21

# Personal notes
1) Problem statement - build a game of war using Python

2) Planning 
    - 2 players, the one who collects all the cards is the winner (Should I implement two player gameplay? 
    How would that even work? Neither of the players even make a move)
    - Shuffle a standard deck of cards with Jokers (need to find a proper shuffling algorithm)
    - Deal out all the cards (Should I do a system where the cards in the odd index goes to one person,
    and the evens go to the other person? This would give a dealing effect (1 to me, 1 to you...))
    - Each player draws a card and displays it simultaneously.
    - Player card with the higest value wins, puts the won cards into a separate pile 
      (What if we prepend these cards to the player's existing deck?)
    - Rank goes from Joker, A, K... 2
    - If the cards are identical in the first "battle"
        - Then this is called War
        - Each player lays down 3 cards and then flips 1 card (4 cards are drawn from the player's deck)
        - Compare the face up card and the highest card wins all
        - If second time identical, then do 3 cards again (Corner case: what happens if not enough cards on the second war, G-O)
        - If player doesn't have cards to put down then they lose the game  
    - (Edge case) - if both players run out of cards before the "war" ends then player with least number of face downs loses, 
      if same number of face downs then the game is a draw or should we face up the last card? hmmm
      
    - I will remove the Jokers for the sake of this implementation
    
    
3) Questions to ask myself (Random thoughts)
   This game can be played without the player even doing anything since everything is done by chance. 
   There is no player decisions or inputs needed.
   - How about letting the user draw cards? But that seems kind of 
   - If a player wins cards, then should I shuffle those cards before adding it to the end of the player's cards? (prepend to the card stack)
   
---

# Planning (Subject to change)
I will make a command line game. If I have time, I will use this game's logic to make a GUI game.

## Standard gameplay
- This is a two player game. The main objective of the game is to collect all the cards.
- The game starts with a shuffled deck of cards with the jokers removed meaning there are 52 cards in the game deck.
- After shuffling the deck, deal out the cards to each player (1 for p1, 1 for p2... etc).
- Each player draws a card from their deck and displays it simultaneously. The player with the highest ranking card wins the pile.
  - Rank goes as follows (high to low): A, K, Q, J... 4, 3, 2, 1.
- The winning player puts the won cards at the bottom of their deck.

## Going to war
- When both players draw the same value card, they go to "war".
- Each player draws 3 cards face down and displays the 4th card. The player with the highest ranking card wins the pile.
- If both players draw the same value card again after the first war, they draw 3 cards each and display the 4th card. This continues until one of the players win.
- If a player does not have enough cards to use for "war", they lose the game.

## Edge Cases and Assumptions
- If both players run out of cards before the "war" ends, then the game ends in a tie.
- If a player wins cards, shuffle the winning cards before adding it to the bottom of the player's cards pile.

# Classes
## Card
### Functions
- Get rank value
- Show card value and suit

## Deck
- Build a deck of cards
- Draw a card from the deck
- Show the cards in the deck (for dev)
- Shuffle the cards

## Player
- Display player name
- Add card into their pile
- Show cards (for dev)
- Pop a card from hand deck
- Prepend won cards into the hand deck

## Game
- Run game
