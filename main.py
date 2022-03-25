from turtle import Turtle, Screen
import time

import SnakeMain

screen= Screen()
screen.setup(width=600, height=600, startx=-300, starty=0)
screen.bgcolor("black")
screen.title("Snake_game_by_TesfayH")

snake = SnakeMain.Snake()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()













screen.exitonclick()