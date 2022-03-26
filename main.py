from turtle import Screen
import time

from SnakeMain import Snake
from food import Food

screen= Screen()
screen.setup(width=600, height=600, startx=-300, starty=0)
screen.bgcolor("black")
screen.title("Snake_game_by_TesfayH")

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()













screen.exitonclick()