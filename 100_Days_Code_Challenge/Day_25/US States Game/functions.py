from turtle import Turtle
import pandas

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv("50_states.csv")
        self.correct_guesses = []
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write("Guess the State", align="center", font=("Arial", 20, "normal"))

    def check_guess(self, guess):
        guess = guess.title()
        if guess in self.data.values:
            self.correct_guesses.append(guess)
            state = self.data[self.data["state"] == guess]
            self.goto(int(state.x), int(state.y))
            self.write(guess)
            return True
        return False

    def get_missing_states(self):
        missing_states = [state for state in self.data["state"] if state not in self.correct_guesses]
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("missing_states.csv")
        