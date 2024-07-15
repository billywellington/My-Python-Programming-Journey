from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes_list = []
        self.create_snake()
        self.head = self.snakes_list[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle()
        snake.speed("slow")
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snakes_list.append(snake)

    def extend(self):
        self.add_snake(self.snakes_list[-1].position())

    def move(self):
        for snake in range(len(self.snakes_list) - 1, 0, -1):
            new_x = self.snakes_list[snake - 1].xcor()
            new_y = self.snakes_list[snake - 1].ycor()
            self.snakes_list[snake].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset_snake(self):
        for snake in self.snakes_list:
            snake.goto(1000, 1000)
        self.snakes_list.clear()
        self.create_snake()
        self.head = self.snakes_list[0]