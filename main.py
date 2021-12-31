from replit import clear
import random
#HINT: You can call clear() to clear the output in the console.

import art


print(art.logo)
bids={}
items = ["car","washdryer","banana"]
again=True



def find_highest_bidder(bids):
  current_highest_bid = 0
  highest_bider=""
  for bidder in bids:
    if bids[bidder] > current_highest_bid:
        current_highest_bid = bids[bidder]
        highest_bider = bidder
  print(f"Highest bidder is {highest_bider} at $ {current_highest_bid}. Congrats you win!")


random_item = random.choice(items)
print(f"Today the item you are bidding for is a {random_item}")
while(again == True):
  name_of_user = input("Enter your Name:\n")
  user_bid = float(input("Enter your Bid $: "))
  bids[name_of_user]=user_bid
  more_bidders = input("Are there any more bidders? (Y) or (N) :\n").lower()
  if more_bidders == "n":
    again=False
    find_highest_bidder(bids)
  else:
    clear()

 


