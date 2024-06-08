# Select a random word from a predefined list.
import random


word_list = ["aardvark", "baboon", "camel"]

# Choose a random word from the list.
word = random.choice(word_list)

# Create a display of underscores representing the letters of the word.
display = ['_'] * len(word)

# Initialize the number of allowed incorrect guesses.
lives = 6

# Initialize an empty list to keep track of guessed letters.
guessed_letters = []

# Initialize a variable to keep track of the game state.
game_over = False

# Print the word for debugging purposes.
print(word)

# Loop until the game is over.

while not game_over:
    # Get a guess from the user.
    guess = input("Guess a letter: ").lower()

    # Check if the guess is a letter and has not already been guessed.
    if guess.isalpha() and guess not in guessed_letters:
        # Add the guessed letter to the list of guessed letters.
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word.
        if guess in word:
            # Update the display with the guessed letter.
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            # Decrement the number of lives if the guessed letter is incorrect.
            lives -= 1
            print(f"Incorrect guess. You have {lives} lives left.")

        # Print the current display.
        print(' '.join(display))

        # Check if the player has won.
        if '_' not in display:
            print("Congratulations! You win!")
            game_over = True

        # Check if the player has run out of lives.
        if lives == 0:
            print("Game over. You lose.")
            game_over = True
    else:
        print("Invalid guess. Please enter a letter you have not already guessed.")

