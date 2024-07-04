class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def breathe(self):
        print(f"{self.name} is breathing")

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"{self.name} is swimming")

    def breathe(self):
        super().breathe()
        print("underwater")

nemo = Fish("Nemo")

nemo.eat()
nemo.swim()
nemo.drink()
nemo.sleep()
nemo.breathe()
