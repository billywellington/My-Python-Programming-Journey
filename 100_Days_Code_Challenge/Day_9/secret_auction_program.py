from art import logo
print(logo)
print("Welcome to the secret auction program.")
print("The program will take bids and determine the highest bidder.")
name = input("Please enter your name.")
bid = int(input("Please enter your bid."))

bidders = {}
bidders[name] = bid

more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

while more_bidders == "yes":
    name = input("Please enter your name.")
    bid = int(input("Please enter your bid."))
    bidders[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

highest_bid = 0
highest_bidder = ""
for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        highest_bidder = bidder

print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}.")






