Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
display = []
for letter in chosen_word:
    if letter == guess:
        display.append(letter)
    else:
        display.append("_")
print(display)
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
