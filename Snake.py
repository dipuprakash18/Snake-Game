from turtle import Screen
from Snake_Class import Snake
import time
from food import Food
from Scoreboard import Scoreboard

screen=Screen()
screen.setup(700,700)
screen.bgcolor("black")
screen.title("Snake Game by Dipu")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting Collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detecting Collision with wall
    if snake.head.xcor()>=330 or snake.head.xcor()<=-335 or snake.head.ycor()>=330 or snake.head.ycor()<=-335:
        game_is_on=False
        scoreboard.game_over()

    # Detecting Collision with Tail
    for i in snake.segments[1:]:
        if snake.head.distance(i)<10:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()