from turtle import Turtle, Screen
import random

color_list = [(246, 242, 244), (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]



# Function to convert RGB tuple to hexadecimal color string
def rgb_to_hex(rgb):
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

# Create turtle and screen objects
dots = Turtle()
screen = Screen()

dots.speed("fast")
dots.width(20)
dots.hideturtle()

def draw_one_line_dots():
# Draw dots with random colors from the color list
    for _ in range(9):
        # Choose a random color from the list
        color = random.choice(color_list)
        # Convert RGB tuple to hexadecimal color string
        hex_color = rgb_to_hex(color)
        # Draw a dot with the chosen color
        dots.dot(20, hex_color)
        # Move the turtle to the next position
        dots.penup()
        dots.forward(50)
        dots.pendown()
        color = random.choice(color_list)
        dots.dot(20, hex_color)

# create a function which sets the heading of the turtle to 225 and
def set_initial_heading():
    dots.setheading(225)
    dots.penup()
    dots.forward(300)
    dots.setheading(0)

#create a function which sets the heading of the turtle to face upwards, move 50 steps forward, face left, move 500 steps forward while drawing no dots
def starting_x_axis():
    dots.setheading(90)
    dots.penup()
    dots.forward(50)
    dots.setheading(180)
    dots.forward(450)



set_initial_heading()
for _ in range(10):
    draw_one_line_dots()
    starting_x_axis()
    dots.setheading(0)


screen.exitonclick()