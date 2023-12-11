

# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.


user_hv = draw_starting_hand("YOUR") 
while user_hv < 21:
  should_hit = input('You have ' + str(user_hv) + ". Hit (y/n)? ")
  if should_hit == 'n':
    break
  elif should_hit == 'y':
    user_hv += draw_card()
  else:
    print("Sorry I didn't get that.")
print_end_turn_status(user_hv)

dealer_hv = draw_starting_hand("DEALER")
while dealer_hv < 17:
  print("Dealer has " + str(dealer_hv) + ".")
  dealer_hv += draw_card()
print_end_turn_status(dealer_hv)

print_end_game_status(user_hv, dealer_hv)


  




