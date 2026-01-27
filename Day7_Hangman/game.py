import random
import hangman_words  # Module containing the list of words
import hangman_art  # Module containing ASCII art for hangman stages and logo

# Get the list of words from the hangman_words module
word_list = hangman_words.word_list

# Total number of wrong guesses allowed
lives = 6

# Print hangman logo at the start
print(hangman_art.logo)

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)

# Initialize display with underscores for each letter in the chosen word
word_length = len(chosen_word)
display = "_" * word_length
print("Word to guess: " + display)

# Flags and lists to track game state
game_over = False
correct_letters = []  # List to store letters guessed correctly
not_contain = []  # List to store letters guessed incorrectly

# Main game loop
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    # Ask player for a letter guess
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in correct_letters or guess in not_contain:
        print("You've already guessed that letter: " + guess)
        continue  # Skip the rest of the loop and ask for another guess

    # Check if guessed letter is in the chosen word
    if guess in chosen_word:
        correct_letters.append(guess)  # Add correct guess to list
    else:
        lives -= 1  # Deduct a life for incorrect guess
        not_contain.append(guess)  # Track incorrect guesses
        print(f"You guessed {guess}, that's not in the word. You lose a life. {lives}/6 ")

    # Build the display string based on correct guesses
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Show current state of the word
    print("Word to guess: " + display)

    # Show hangman stage corresponding to remaining lives
    print(hangman_art.stages[lives])

    # Check win condition
    if "_" not in display:
        game_over = True
        print("Congratulations,you win!!!")

    # Check lose condition
    if lives == 0:
        game_over = True
        print(f"***********************YOU LOSE**********************\nThe correct word is {chosen_word}")
