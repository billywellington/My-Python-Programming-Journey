from abc import ABC, abstractmethod

class Vehicle:

    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You dive the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You drive the motorcycle")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()

