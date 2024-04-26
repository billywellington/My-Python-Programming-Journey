class Player:
    def __init__(self, name, health, score):
        self.name = name
        self.health = health
        self.score = score

    def attack(self, target):
        print(f"{self.name} attacks {player2.name}!")

    def heal(self):
            self.health += 10
            print(f"{self.name} heals. Health is now {self.health}.")

class Wizard(Player):
    def cast_spell(self, target):
        print(f"{self.name} casts a spell on {target.name}")
# Creating player objects

player1 = Player("Alice", 100, 0)
player2 = Player("Bob", 80, 0)
wizard1 = Wizard("Charlie", 70, 0)

# Example of using methods with objects
# player1.attack(player2)
# player2.heal()

wizard1.attack(player1)
wizard1.cast_spell(player2)
