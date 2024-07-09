import turtle

# Set up the turtle
t = turtle.Turtle()

# Draw a line
t.speed(1)
t.forward(100)

# Teleport to a new location (instantaneous, no line drawn)
t.teleport(200, 200)

# Draw another line
t.speed(1)
t.forward(100)

# Keep the window open until clicked
turtle.done()
