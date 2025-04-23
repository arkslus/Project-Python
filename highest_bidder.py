# Import the logo
from art import logo

# Print the ASCII art logo
print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# initialize an empty dictionary to store auction data
auction_bids = {}

# Continue asking for bids until the user chooses not to
continue_bidding = True
while continue_bidding:
    # Ask for the username
    username = input("Enter your username: ")
    # Ask for the bid price
    bid_price = float(input("Enter the bid price: $"))
    # Add name and bid price to the dictionary
    auction_bids[username] = bid_price
    # Ask if the user wants to bid again
    should_bid = input("Do you want to bid again? (yes/no): \n").lower()
    # If the user chooses not to bid, find and print the winner
    if should_bid == "no":
        continue_bidding = False
        find_highest_bidder(auction_bids)
    elif should_bid == "yes":
        print("\n" * 20)
