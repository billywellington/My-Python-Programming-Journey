# Objective:
# Implement a function that takes an object representing a bird and outputs the sound it makes. The function should work with any object that has a make_sound method.

# Instructions:

# Define a Duck class with a make_sound method that prints "Quack!".
# Define a Goose class with a make_sound method that prints "Honk!".
# Define a Person class with a make_sound method that prints "I'm quacking like a duck!".
# Implement a function called make_bird_sound that takes a bird object as an argument and calls its make_sound method.
# Test your function with instances of Duck, Goose, and Person classes to ensure it works correctly.


class Duck:
        
    def make_sound(self):
        print("Quack!")

class Goose:
        
    def make_sound(self):
        print("Honk!")

class Person:
        
    def make_sound(self):
        print("I'm quacking like a duck!")

def make_bird_sound(bird):
    bird.make_sound()

# Test the function
print("Duck:")
duck = Duck()
make_bird_sound(duck)  # Output: Quack!

print("\nGoose:")
goose = Goose()
make_bird_sound(goose)  # Output: Honk!

print("\nPerson:")
person = Person()
make_bird_sound(person)  # Output: I'm quacking like a duck!