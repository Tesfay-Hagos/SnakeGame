STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle, Screen
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0

class Snake:
    screen = Screen()
    screen.tracer(0)

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            ob = Turtle("square")
            ob.color("white")
            ob.penup()
            ob.goto(position)
            self.snake.append(ob)

    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for seq_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seq_num - 1].xcor()
            new_y = self.snake[seq_num - 1].ycor()
            self.snake[seq_num].goto(new_x, new_y)
        self.head.forward(20)
