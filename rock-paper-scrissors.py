# This program intends to reproduce the rock-paper-scissors game

import random

options = ["rock", "paper", "scissors"]


bot = random.choice(options)
player = None
play_again = "yes"
main_score = 0
player_score = 0
bot_score = 0


print("Welcome to Billy's version of the well known Rock-Paper_Scissors Game.\n")

player_name = (input("Please type in your name:  "))

print("In this game, you'll face off with my computer, we'll call him 'Bot'. \n\nFor each round we'll display the scoreboard and each win has 2 points, a tie has one points. \nPlease follow the instruction given below. \n\nIf you want to quite the game, please type in 'No' after you're prompted to play again. \nYou can only exit the game after a round is complete. ENJOY IT, " + player_name)

print("\n\n################### " + player_name.upper() + " VS BOT ###################\n")
# print("\n\n################### START GAME ###################\n")

# print()

while play_again == "yes":

    player = input("\nRock, Paper, or Scissors? Choose one: ").lower()

    while player not in options:
        player = input("Please choose only from the 3 following options: Rock, Paper, or Scissors >> ").lower()

    if player == "rock":
        if bot == "rock":
            print("The bot chose: ", bot)
            print("You chose : ", player)
            print("It's a tie!\n")
            bot_score = bot_score + 1
            player_score =  player_score + 1

            print("________________________________")
            print("SCOREBOARD")
            print("________________________________\n")

            print(player_name + ": " + str(player_score) + " | Bot: " + str(bot_score) )

        elif bot == "paper":
            print("The bot chose: ", bot)
            print("You chose : ", player)
            print("You lost! Bot win!")

            bot_score = bot_score + 2
            player_score = player_score

            print("________________________________")
            print("SCOREBOARD")
            print("________________________________\n")

            print(player_name + ": " + str(player_score) + " | Bot: " + str(bot_score))

        else:
            print("The bot chose: ", bot)
            print("You chose : ", player)
            print("You won! Bot lost!")

            bot_score = bot_score
            player_score = player_score + 2

            print("________________________________")
            print("SCOREBOARD")
            print("________________________________\n")

            print(player_name + ": " + str(player_score) + " | Bot: " + str(bot_score))

    elif player == "scissors":
        if bot == "rock":
            print("The bot chose: ", bot)
            print("You chose : ", player)
            print("You won! Bot lost!")

            bot_score = bot_score
            player_score = player_score + 2

            print("________________________________")
            print("SCOREBOARD")
            print("________________________________\n")

            print(player_name + ": " + str(player_score) + " | Bot: " + str(bot_score))

        elif bot == "paper":
            print("The bot chose: ", bot)
            print("You chose : ", player)
            print("You lost! Bot win!")

            bot_score = bot_score + 2
            player_score = player_score

            print("________________________________")
            print("SCOREBOARD")
            print("________________________________\n")

            print(player_name + ": " + str(player_score) + " | Bot: " + str(bot_score))

        else:
            print("The bot chose: ", bot)
            print("You chose : ", player)
            print("It's a tie!")

            bot_score = bot_score + 1
            player_score = player_score + 1

            print("________________________________")
            print("SCOREBOARD")
            print("________________________________\n")

            print(player_name + ": " + str(player_score) + " | Bot: " + str(bot_score))

    else: #player == "paper"
        if bot == "rock":
            print("The bot chose: ", bot)
            print("You chose : ", player)
            print("You won! Bot lost!")

            bot_score = bot_score
            player_score = player_score + 2

            print("________________________________")
            print("SCOREBOARD")
            print("________________________________\n")

            print(player_name + ": " + str(player_score) + " | Bot: " + str(bot_score))

        elif bot == "scissors":
            print("The bot chose: ", bot)
            print("You chose : ", player)
            print("You lost! Bot win!")

            bot_score = bot_score + 2
            player_score = player_score

            print("________________________________")
            print("SCOREBOARD")
            print("________________________________\n")

            print(player_name + ": " + str(player_score) + " | Bot: " + str(bot_score))

        else:
            print("The bot chose: ", bot)
            print("You chose : ", player)
            print("It's a tie!")

            bot_score = bot_score + 1
            player_score = player_score + 1

            print("________________________________")
            print("SCOREBOARD")
            print("________________________________\n")

            print(player_name + ": " + str(player_score) + " | Bot: " + str(bot_score))

    play_again = input("\nDo you want to play again? Yes/No: ").lower()
print("\n________________________________")
print("FINAL SCOREBOARD!!!!!")
print("________________________________\n")

print(player_name + ": " + str(player_score) + " | Bot: " + str(bot_score))
if player_score > bot_score:
    print("You are the champion, " + player_name +" Well done, mate!")
else:
    print("You are the runner-up, " + player_name)
    print("Bye! Bye!")

print("\n\n################### END GAME ###################\n")
