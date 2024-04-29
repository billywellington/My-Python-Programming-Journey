# Exercise 1: Creating a Simple Class
# Question:
# Define a Python class named Rectangle. This class should have:
#
# Two attributes: width and height, representing the width and height of the rectangle.
# A method named area() that calculates and returns the area of the rectangle.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle1 = Rectangle(4, 3)

print("The area of the rectangle is: " +str(rectangle1.area()))

