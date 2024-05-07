# Question:
# Building upon the Rectangle class from Exercise 1, add the following functionality:
#
# A method named perimeter() that calculates and returns the perimeter of the rectangle.
# A method named scale() that takes a scale factor as a parameter
# and scales both the width and height of the rectangle by that factor.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    # A method named scale() that takes a scale factor as a parameter
    # and scales both the width and height of the rectangle by that factor.
    def scale(self):
        print("The new width scaled by value of " + str(self.perimeter()) + " is: " + str(self.perimeter() * self.width))
        print("The new height scaled by value of " + str(self.perimeter()) + " is: " + str(self.perimeter() * self.height))



rectangle1 = Rectangle(4, 3)

print("The area of the rectangle is: " +str(rectangle1.area()))
print("The area of the perimeter is: " +str(rectangle1.perimeter()))
rectangle1.scale()


