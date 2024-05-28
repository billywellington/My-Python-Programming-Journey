# Objective:
# Create a function that simulates a race between different vehicles. The function should take a list of vehicles and output the winner based on their speed.

# Instructions:

# Define a Car class with a speed attribute representing the car's speed.
# Define a Bike class with a speed attribute representing the bike's speed.
# Define a Boat class with a speed attribute representing the boat's speed.
# Implement a function called race that takes a list of vehicles and determines the winner based on their speed.
# Test your function with instances of Car, Bike, and Boat classes to ensure it works correctly.

class Car:
    def __init__(self, speed):
        self.speed = speed

class Bike:
    def __init__(self, speed):
        self.speed = speed


class Boat:
    def __init__(self, speed):
        self.speed = speed


list_of_speed = []

def race():
    list_of_speed.sort()
    print("Winner of this race is:", list_of_speed[-1])

car = Car(180)
list_of_speed.append(car.speed)

boat = Boat(200)
list_of_speed.append(boat.speed)

bike = Bike(360)
list_of_speed.append(bike.speed)
race()
