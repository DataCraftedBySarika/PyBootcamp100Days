# Import the art module to display the logo
import art


print(art.logo)

# Dictionary to store bidder names and their bid amounts
all_bid_details = {}

# Flag to control the while loop
should_continue = True

# Keep asking for bids until there are no more bidders
while should_continue:
    # Ask for bidder's name
    name = input("What is your name?: ")

    # Ask for bidder's bid amount and convert it to integer
    bid_amount = int(input("What is your bid $?: "))

    # Store the bid amount using name as the key
    all_bid_details[name] = bid_amount

    # Ask if there are more bidders
    continue_people = input("Are there any other bidders? Type 'yes' or 'no': ")

    # Clear the screen by printing blank lines
    print('\n' * 100)

    # If no more bidders, stop the loop
    if continue_people == 'no':
        should_continue = False

# Variables to track the highest bid and the winner's name
max_name = ''
max_bidamount = 0

# Loop through the dictionary to find the highest bid
for name, bid in all_bid_details.items():
    # If the current bid is higher than the max bid so far
    if bid > max_bidamount:
        max_bidamount = bid
        max_name = name

# Print the winner and the highest bid
print(f"The winner is {max_name} with a bid of ${max_bidamount}")
