from turtle import Turtle, Screen
import random

#create a list called colors with 20 strings representing colou names accordign to trinket documentation
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "black", "brown", "grey", "cyan", "magenta", "violet", "indigo", "turquoise", "maroon", "gold", "silver", "lime", "teal"]
tom = Turtle()
screen = Screen()
screen.bgcolor("white")

#set the arrow to start at the center of the screen


tom.speed(3.5)
tom.width(10)

for _ in range(80):
    tom.color(random.choice(colors))
    tom.forward(30)
    tom.setheading(random.choice([0, 90, 180, 270]))

screen.exitonclick()

