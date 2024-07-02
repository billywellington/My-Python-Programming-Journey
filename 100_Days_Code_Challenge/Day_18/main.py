from turtle import Turtle, Screen

tom = Turtle()

screen = Screen()
screen.bgcolor("white")
# timmy.shape("arrow")
# timmy.color("black")
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
#

#create a triangle
for _ in range(3):
    tom.forward(100)
    tom.right(120)

# create a square, with a different color
tom.color("red")
for _ in range(4):
    tom.forward(100)
    tom.right(90)

# create a pentagon with a different color
tom.color("blue")
for _ in range(5):
    tom.forward(100)
    tom.right(72)

# create a hexagon with a different color
tom.color("green")
for _ in range(6):
    tom.forward(100)
    tom.right(60)

# create a heptagon with a different color
tom.color("purple")
for _ in range(7):
    tom.forward(100)
    tom.right(51.43)

# create a octagon with a different color
tom.color("orange")
for _ in range(8):
    tom.forward(100)
    tom.right(45)

# create a nonagon with a different color
tom.color("black")
for _ in range(9):
    tom.forward(100)
    tom.right(40)

# create a decagon with a different color
tom.color("brown")
for _ in range(10):
    tom.forward(100)
    tom.right(36)







screen.exitonclick()


