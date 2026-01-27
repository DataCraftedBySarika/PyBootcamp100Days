# Hangman Game in Python

A simple **Hangman** game built in Python. 
Players guess letters to reveal a hidden word before running out of lives. 
The game features ASCII art for the hangman and a dynamic display of guessed letters.

## Features

- Randomly selects a word from a predefined list (`hangman_words`)
- ASCII art representation of hangman (`hangman_art`)
- Tracks correct and incorrect guesses
- Prevents duplicate guesses
- Shows remaining lives
- Win/lose messages with correct word reveal


## File Structure

1. game.py # Main game script
2. hangman_words.py # Contains the list of words for the game
3. hangman_art.py # Contains ASCII art for hangman stages and logo

## How to Play

1. Run the game script. 
2. Guess letters one at a time. 
3. You have 6 lives. Each wrong guess costs a life. 
4. Guess all letters correctly to win, or lose all lives to lose.