from turtle import Turtle
with open("data.txt") as data:
    content = data.read()



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(content)
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.update_scoreboard()