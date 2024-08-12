from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snakes = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snakes.up, "w")
screen.onkey(snakes.down, "s")
screen.onkey(snakes.left, "a")
screen.onkey(snakes.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakes.move()

    # Detect collision with food
    if snakes.head.distance(food) < 15:
        food.refresh()
        snakes.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snakes.head.xcor() > 295 or snakes.head.xcor() < -295 or snakes.head.ycor() > 295 or snakes.head.ycor() < -295:
        snakes.reset_snake()
        scoreboard.reset_score()

    # Detect collision with tail
    for snake in snakes.snakes_list[1:]:
        if snakes.head.distance(snake) < 10:
            snakes.reset_snake()
            scoreboard.reset_score()


screen.exitonclick()
