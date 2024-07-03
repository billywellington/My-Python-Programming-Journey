from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Racing Game")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win")
print(f"You have bet on {user_bet}. Let's see who wins!")


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
turtle_names = []

for item in colors:
    current_turtle = names[colors.index(item)]
    current_turtle = Turtle(shape="turtle")
    current_turtle.color(item)
    current_turtle.penup()
    current_turtle.width(5)
    current_turtle.goto(x=-239, y=-100 + colors.index(item) * 40)
    turtle_names.append(current_turtle)

if user_bet:
    is_game_on = True
    print("Game is on!")

while is_game_on:
        for turtle in turtle_names:
            if turtle.xcor() > 230:
                is_game_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print("Game Over!")
                    print(f"You've won! The {winning_color} turtle won!")
                else:
                    print("Game Over!")
                    print(f"You've lost! The {winning_color} turtle won!")
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)



screen.exitonclick()