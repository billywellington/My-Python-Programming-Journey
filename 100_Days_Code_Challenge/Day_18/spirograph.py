from turtle import Turtle, Screen
import random

#create a list called colors with 20 strings representing colou names accordign to trinket documentation
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "black", "brown", "grey", "cyan", "magenta", "violet", "indigo", "turquoise", "maroon", "gold", "silver", "lime", "teal"]


tom = Turtle()
screen = Screen()
screen.bgcolor("white")
tom.speed("fastest")
tom.width(2)

for _ in range(360):
    tom.color(random.choice(colors))
    tom.circle(100)
    tom.setheading(tom.heading() + 10)










screen.exitonclick()
