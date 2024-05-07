# Exercise 6: Designing a Car Class
# Question:
# Define a Python class named Car to represent a car. The Car class should have:
#
# Attributes for make, model, year, and mileage.
# Methods named drive() and display_info().
# The drive() method should take a distance in miles as input and update the mileage attribute accordingly.
# The display_info() method should print out the make, model, year, and current mileage of the car.

class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    # The drive() method should take a distance in miles as input and update the mileage attribute accordingly.

    def drive(self, distance):
        self.distance = distance
        self.mileage += self.distance
        print(f"This {self.model} is driving {self.distance} miles.\nNew mileage is {self.mileage} miles\n")

    # The display_info() method should print out the make, model, year, and current mileage of the car.
    def display(self):
        print(f"| About This Car |\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nCurrent Mileage: {self.mileage}\n\n")

car1 = Car("Thunderbolt", "Lightning X", 2013, 31287)
car2 = Car("Horizon", "Nova G", 2023, 35000)
car3 = Car("Phoenix", "Fusion R", 2003, 30000)
car4 = Car("Apex", "Blaze S", 2033, 36000)

car1.drive(2000)
car1.display()

car2.drive(3000)
car2.display()

car3.drive(4000)
car3.display()

car4.drive(2500)
car4.display()