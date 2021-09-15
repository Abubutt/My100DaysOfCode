from art import logo
import os
auctions = {}
bid = True

print(logo)
print("Welcome to the secret auction program")

while bid:
    name = input("What is your name? ")
    bid_price = int(input("What is your bid? $"))
    auctions[name] = bid_price
    other_bidders = input("Are there any other bidders? (Y/N) ")
    if other_bidders == "N":
        bid = False
        os.system("clear")
    else:
        os.system("clear")

highest_bid = 0

for bidder in auctions:
    bid_amount = auctions[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")
