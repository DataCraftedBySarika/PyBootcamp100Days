# Day 11 – Blackjack Game ♠️🃏

## 📌 Project Overview

The goal is to build a **command-line Blackjack game** using Python while applying concepts such as:

* Functions
* Loops
* Conditional logic
* Lists
* Randomization
* Clean code structure

The game follows **real Blackjack rules**, including proper Ace handling and Blackjack detection.

## 🎯 Game Rules

* The game is played between **Player** and **Dealer (Computer)**.
* Cards have the following values:

  * Number cards (2–10): face value
  * Jack, Queen, King: 10
  * Ace: 11 or 1 (automatically adjusted)
* **Blackjack** occurs when a player gets **21 with the first two cards only**.
* The player can:

  * Type `y` to draw another card (Hit)
  * Type `n` to stop drawing cards (Stand)
* The dealer:

  * Must draw cards until their score is **17 or higher**.


## 🧠 Key Logic Implemented

### ✔ Ace Handling

If the total score exceeds 21 and the hand contains an Ace (11), the Ace is converted to 1 automatically.

### ✔ Blackjack Check

* Blackjack is only declared if:

  * Score is 21
  * Hand contains **exactly two cards**

### ✔ Win Conditions

* Player busts → Player loses
* Dealer busts → Player wins
* Blackjack beats normal 21
* Higher score wins if neither busts
* Same score → Draw

## Features

* Function-based design
* Realistic Blackjack rules
* Replay option after each game
* Clean and readable output
* Beginner-friendly structure


### Main Functions

* `deal_card()` – Returns a random card
* `calculate_score(hand)` – Calculates score and adjusts Aces
* `compare_scores(player_hand, dealer_hand)` – Decides the winner
* `play_game()` – Controls one full round of Blackjack


## Example Gameplay

```text
Your cards: [10, 11], current score: 21
Computer's first card: 7
Win with a Blackjack 🎉
```

## 🚀 Learning Outcomes

By completing this project, you will understand:

* How to break a problem into functions
* How to manage game state using loops
* How to apply real-world rules in code
* Why clean function naming and return values matter



