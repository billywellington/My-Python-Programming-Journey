from art import logo
import random

#TODO1: Print the logo and a welcome message to the user.

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#TODO3: Generate and store a random number between 1 and 100.
random_number = random.randint(1, 100)

#TODO3.1: Ask the user to choose a difficulty level 
# and set the number of attempts based on the difficulty level.
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5


#TODO2: Ask the user to guess a number between 1 and 100.
#TODO6: If the user's guess is higher than the random number, tell them their guess is too high.
#TODO7: If the user's guess is lower than the random number, tell them their guess is too low.
#TODO8: If the user's guess is equal to the random number, tell them they've guessed it right.

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess > random_number:
        print("Too high.")
    elif user_guess < random_number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {random_number}.")
        break
    #TODO9: Track the number of turns remaining.
    attempts -= 1
    if attempts == 0:
        print("You've run out of guesses. You lose.")
        break
    print("Guess again.")
