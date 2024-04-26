
#this program shows that each child will use a method that's closely related to itself.
class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()