
from turtle import Turtle
from SnakeMain import Snake
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode='r') as H_score:
            self.high_score = int(H_score.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode='w') as H_score:
                H_score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()





