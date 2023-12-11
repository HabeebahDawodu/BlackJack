# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint
# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:

# Return:
#   none
def print_card_name(card_rank):
    if card_rank == 1:
        print("Drew an Ace")
    elif card_rank == 11:
        print("Drew a Jack")
    elif card_rank == 12:
        print("Drew a Queen")
    elif card_rank == 13:
        print("Drew a King")
    elif card_rank >= 2 and card_rank <= 7 or card_rank >= 9 and card_rank <= 10:
        print("Drew a " + str(card_rank))
    elif card_rank == 8:
        print("Drew an " + str(card_rank))
    elif card_rank > 13:
        print("BAD CARD")

# Draws a new random card, prints its name, and returns its value.
# card_rank = randint(1, 13)

# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
    card_rank = randint(1,13)
    print_card_name(card_rank)
    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        return 10
    elif card_rank == 1:
        return 11
    else:
        return card_rank

# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
# 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
    print("-----------")
    print(message)
    print("-----------")
    
# Prints turn header and draws a starting hand, which is two cards.
#
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.

def draw_starting_hand(name):
    print_header(name.upper() + " TURN")
    card_1 = draw_card()
    card_2 = draw_card()
    hand_value = card_1 + card_2
    return hand_value
#hand_value = draw_card(card1_rank) + draw_card(card2_rank)    
# Prints the hand total and status at the end of a player's turn.
# 
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
    print("Final hand: " + str(hand_value) + ".")
    if hand_value == 21:
        print("BLACKJACK!")
    elif hand_value > 21:
        print("BUST.")

# Prints the end game banner and the winner based on the final hands.
# 
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand, dealer_hand):
    print_header("GAME RESULT")
    if user_hand == 21 and player_hand == 21:
        print("Push.")
    if user_hand == 21 and dealer_hand > 21:
        print("You win!")
    if user_hand > 21 and dealer_hand == 21:
        print("Dealer wins!")
    if user_hand > 21 and dealer_hand > 21:
        print("Dealer wins!")
    # When player and dealer neither BLACKJACK or BUST.
    elif user_hand > dealer_hand and user_hand < 21:
        print("You win!")
    elif user_hand < dealer_hand and dealer_hand < 21:
        print("Dealer wins!")
    elif user_hand == dealer_hand and dealer_hand < 21:
        print("Push.")
    # When dealer BLACKJACKs or BUSTs player does neither.
    elif dealer_hand > 21 and user_hand < 21:
        print("You win!")
    elif dealer_hand == 21 and user_hand < 21:
        print("Dealer win!")
    # When player BLACKJACKs or BUSTs dealer does neither.
    elif dealer_hand < 21 and user_hand > 21:
        print("Dealer wins!")
    elif dealer_hand < 21 and user_hand == 21:
        print("You win!") 
    # Implement print_end_game_status function here
