from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")

ball = Turtle("circle")
ball.color("white")
ball.goto(0, 0)
ball.right(45)
# ball.speed(1)
ball.penup()
# ball.teleport(350,280, fill_gap=True)
ball.goto(350, 280)

screen.exitonclick()