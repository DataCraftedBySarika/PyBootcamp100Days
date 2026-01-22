# Import random module to let the computer make a random choice
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store all gestures in a list (index-based access)
gesture = [rock, paper, scissors]

# Names of gestures for display
gesture_names = ["Rock", "Paper", "Scissors"]

# Ask the user to choose a gesture (0, 1, or 2)
user = int(input("Choose 0 Rock, 1 Paper, 2 Scissors? "))

# Validate user input
if user >= 0 and user <= 2:

    # Display user's choice
    print(f"You have chosen: {gesture_names[user]}")
    print(gesture[user])

    # Generate random choice for computer (0, 1, or 2)
    computer = random.randint(0, 2)

    # Display computer's choice
    print(f"Computer has chosen: {gesture_names[computer]}")
    print(gesture[computer])

    # Check for draw condition
    if user == computer:
        print("It's a draw")

    # Check winning conditions for the user
    elif (user == 0 and computer == 2) or \
            (user == 1 and computer == 0) or \
            (user == 2 and computer == 1):
        print("Hurrah!Congratulations, you win!")

    # If none of the above, user loses
    else:
        print("Oops,You lose")

# If user enters an invalid number
else:
    print("Invalid number.Please choose 0, 1, or 2.")


