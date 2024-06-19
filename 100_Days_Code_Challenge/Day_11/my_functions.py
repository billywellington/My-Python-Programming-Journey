import random
import os

def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def check_blackjack(user_cards, dealer_cards):
    if 11 in user_cards and 10 in user_cards:
        return "Blackjack! You win!"
        
    elif 11 in dealer_cards and 10 in dealer_cards:
        return "Dealer has Blackjack! You lose!"
    else:
        return False

"""Create a function called compare() and pass in the user_score and dealer_score. 
If the computer and user both have the same score, then it's a draw. 
If the computer has a blackjack (0), then the user loses. 
If the user has a blackjack (0), then the user wins. 
If the user_score is over 21, then the user loses. 
If the dealer_score is over 21, then the computer loses. 
If none of the above, then the player with the highest score wins."""

def compare(user_score, dealer_score):
    #Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"


    if user_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game(user_cards, dealer_cards, user_score, dealer_score):
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    
    if check_blackjack(user_cards, dealer_cards) == False:
        #if user_score is greater than 21
        if user_score > 21:
            #if they have an ace
            if 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
                user_score = calculate_score(user_cards)
                #if the new user_score is still greater than 21 and has an ace
                if user_score > 21:
                    print(f"Your cards: {user_cards}, current score: {user_score}")
                    print("You went over. You lose.")
                #if score is less than 21 and has an ace, ask user if they want to pick another card
                else:
                    answer = input("Do you want to pick another card? Type 'y' or 'n': ")
                    if answer == 'y':
                        user_cards.append(deal_card())
                        print(f"Your current cards: {user_cards}")
                        user_score = calculate_score(user_cards)
                        #start again at adding the 2 scores and checking for blackjack  
                        play_game(user_cards, dealer_cards, user_score, dealer_score)
                    
                    else:
                        #if user says no
                        #dealer picks cards until score is 17 or more
                        dealer_cards.append(deal_card())
                        #calculate dealer score
                        dealer_score = calculate_score(dealer_cards)
                        while dealer_score < 17:
                            dealer_cards.append(deal_card())
                            dealer_score = calculate_score(dealer_cards)
                        if dealer_score > 21:
                            print("Dealer went over. You win!")
                        else:
                            print(f"Your final hand: {user_cards}, final score: {user_score}")
                            print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
                            if user_score > dealer_score:
                                print("You win!")
                            elif user_score < dealer_score:
                                print("You lose!")
                            else:
                                print("It's a draw!")
            else:
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print("You went over. You lose.")
        else:
            #if score is less than 21 after checking for blackjack and none is found
            answer = input("Do you want to pick another card? Type 'y' or 'n' only: ")
            if answer == 'y':
                user_cards.append(deal_card())
                print(f"Your current cards: {user_cards}")
                user_score = calculate_score(user_cards)
                #start again at adding the 2 scores and checking for blackjack
                play_game(user_cards, dealer_cards, user_score, dealer_score)
            else:
                #if user says no
                #dealer picks cards until score is 17 or more
                dealer_cards.append(deal_card())
                while dealer_score < 17:
                    dealer_cards.append(deal_card())
                    dealer_score = calculate_score(dealer_cards)
                if dealer_score > 21:
                    print("Dealer went over. You win!")
                else:
                    print(f"Your final hand: {user_cards}, final score: {user_score}")
                    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
                    if user_score > dealer_score:
                        print("You win!")
                    elif user_score < dealer_score:
                        print("You lose!")
                    else:
                        print("It's a draw!")
    else:
        print(check_blackjack(user_cards, dealer_cards))
        return