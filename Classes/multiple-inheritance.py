class Animal():
    def animal_kindgom(self):
        print("This is part of the animal kingdom")

class Prey(Animal):
    def prey(self):
        print("This animal is a prey")

class Predator(Animal):
    def predator(self):
        print("This animal is a predator")


class Mouse(Prey):
    pass
class Cat(Prey, Predator):
    pass
class Snake(Predator):
    pass

mouse = Mouse()
cat = Cat()
snake = Snake()

#mouse.animal_kindgom()
#mouse.prey()

# cat.animal_kindgom()
# cat.prey()
# cat.predator()

snake.animal_kindgom()
snake.predator()