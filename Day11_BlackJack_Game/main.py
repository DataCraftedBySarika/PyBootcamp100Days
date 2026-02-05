import random
import art

# List representing a deck of cards
# 11 is Ace, face cards (J, Q, K) are worth 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    # Returns a random card from the deck
    return random.choice(cards)


def calculate_score(hand):
    # Calculates the total score of a hand.Converts Ace (11) to 1 if score goes above 21.
    score = sum(hand)

    # Adjust Ace value if the score exceeds 21
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)

    return score


def compare_scores(player_hand, dealer_hand):
    # Compares final player and dealer scores and returns the result message.
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    # Player busts
    if player_score > 21:
        return "Player Bust. You went over. You lose "

    # Dealer busts
    if dealer_score > 21:
        return "Opponent Bust. Dealer went over. You win"

    # Check for Blackjack (only first two cards)
    if player_score == 21 and len(player_hand) == 2:
        return "Win with a Blackjack 🎉"
    if dealer_score == 21 and len(dealer_hand) == 2:
        return "Lose, opponent has Blackjack "

    # Compare scores
    if player_score == dealer_score:
        return "Draw "
    elif player_score > dealer_score:
        return "You win "
    else:
        return "You lose "


def play_game():
    """
    Controls the full flow of one Blackjack game.
    """
    print("\n" * 20)
    print(art.logo)
    print("Welcome to Blackjack!")

    # Initial dealing of two cards each
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    game_over = False

    # Player's turn
    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        # End game if Blackjack or bust
        if player_score == 21 or player_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")

            if choice == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    # Dealer's turn (only if player hasn't busted)
    while calculate_score(dealer_cards) < 17 and calculate_score(player_cards) <= 21:
        dealer_cards.append(deal_card())

    # Final results
    print(f"\nYour final hand: {player_cards}, final score: {calculate_score(player_cards)}")
    print(f"Computer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")

    print(compare_scores(player_cards, dealer_cards))


# Main game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
