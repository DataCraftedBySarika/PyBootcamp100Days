# This will display the cipher logo when the program runs
import art
print(art.logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Caesar cipher function
# original_text: text entered by the user
# shift_amount: number of positions to shift each letter
# encode_or_decode: decides whether to encrypt or decrypt
def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""  # stores the final encrypted/decrypted text

    # If decoding, reverse the shift direction
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Loop through each character in the input text
    for letter in original_text:

        # If the character is a letter, shift it
        if letter in alphabet:
            # Find the letter's position and apply the shift
            shifted_position = alphabet.index(letter) + shift_amount

            # Use modulo to wrap around the alphabet
            shifted_position %= len(alphabet)

            # Add the shifted letter to the result
            cipher_text += alphabet[shifted_position]
        else:
            # If it's not a letter (number, symbol, space), keep it as is
            cipher_text += letter

    # Display the final result
    print(f"\nHere is the {encode_or_decode}d result: {cipher_text}\n")



should_continue = True

# Keep running the program until the user chooses to stop
while should_continue:

    # Ask user whether to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Keep asking until a valid option is entered
    while direction not in ["encode", "decode"]:
        direction = input("Invalid input. Type 'encode' or 'decode':\n").lower()

    # Get the message from the user
    text = input("Type your message:\n").lower()

    # Ask for shift number and validate it
    while True:
        shift_input = input("Type the shift number(only numbers accepted):\n")

        # Check if input contains only digits
        if shift_input.isdigit():
            shift = int(shift_input)

            # Reduce large shift values (e.g., 52 → 0)
            shift %= len(alphabet)
            break
        else:
            print("Numbers only please.")

    # Call the Caesar cipher function
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to restart the program
    restart = input("Do you want to restart the cipher program? yes or no:\n").lower()

    # Stop the loop if the user does not want to continue
    if restart != "yes":
        should_continue = False
        print("\nThank you!! See you next time 👋")
