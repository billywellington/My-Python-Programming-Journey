import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Move the turtle to a new location
my_turtle.forward(100)

# Create a stamp at the current location
my_turtle.stamp()

# Move the turtle again
my_turtle.right(90)
my_turtle.forward(50)

# Create another stamp
my_turtle.stamp()

my_turtle.right(90)
my_turtle.forward(50)
my_turtle.penup()
my_turtle.home()
# Keep the window open until it is clicked
turtle.done()
