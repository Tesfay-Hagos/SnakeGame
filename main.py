from turtle import Screen
import time
from scoreboard import ScoreBoard
from SnakeMain import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600, startx=-300, starty=0)
screen.bgcolor("black")
screen.title("Snake_game_by_TesfayH")

snake = Snake()
food = Food()
score_board = ScoreBoard()
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

    if snake.head.distance(food) < 15:
        food.random_move()
        score_board.increase_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()















screen.exitonclick()