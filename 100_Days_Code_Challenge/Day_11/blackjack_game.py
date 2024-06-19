import random
import os
import art
from my_functions import calculate_score, deal_card, check_blackjack, play_game, clear


#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
#If they answer no, exit the game.
answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while answer == 'y':
    clear()
    user_cards = []
    dealer_cards = []

    for x in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
    print(art.logo)

    print(f"Your cards: {user_cards}")
    print(f"Dealer's first card: {dealer_cards[0]}")
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    play_game(user_cards, dealer_cards, user_score, dealer_score)
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")