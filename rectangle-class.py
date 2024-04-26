# Define a Python class named Rectangle. This class should have:
#
# Two attributes: width and height, representing the width and height of the rectangle.
# A method named area() that calculates and returns the area of the rectangle.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)
polygon = Rectangle(4, 5)
polygon.area()
print("The area is: " + str(polygon.area()))