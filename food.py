from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.random_move()

    def random_move(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(x=random_x, y=random_y)


