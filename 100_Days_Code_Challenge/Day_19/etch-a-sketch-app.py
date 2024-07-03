from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


#create a function to move forward
def move_forward():
    tim.forward(50)

#listen to the letter w key press
screen.onkey(key="w", fun=move_forward)


#create a function to move backward
def move_backward():
    tim.backward(50)

#listen to the letter s key press
screen.onkey(key="s", fun=move_backward)


#create a function to move clockwise
def move_clockwise():
    tim.right(10)

#listen to the letter d key press
screen.onkey(key="d", fun=move_clockwise)

#create a function to move counter clockwise
def move_counter_clockwise():
    tim.left(10)

#listen to the letter a key press
screen.onkey(key="a", fun=move_counter_clockwise)


#create a function to clear the screen
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

#listen to the letter c key press
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()