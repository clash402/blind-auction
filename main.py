import os

from art import logo


# METHODS
def find_highest_bid(final_bids):
    highest_bidder = ""
    highest_bid = 0

    for key, value in sorted(final_bids.items()):
        if value > highest_bid:
            highest_bidder = key
            highest_bid = value

    return f"The highest bidder is {highest_bidder} with ${highest_bid}."


# MAIN
print(logo)
print("Welcome to the secret auction.")

bids = {}
bidding_is_in_progress = True

while bidding_is_in_progress:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bids[name] = bid

    if input("Are there any other bidders? (y/n) ").lower() == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        bidding_is_in_progress = False

winner = find_highest_bid(bids)

print(winner)
