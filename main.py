from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game🐍🐍")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#     Detect collision with the food
    if snake.head.distance(food)<15:
        print("num num")
        food.refresh()
        score.increase_score()
        snake.extend()

#     Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

#     Detect collision with tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
#     if head collide with any segment in tail
#     trigger game_is_on =false
            game_is_on = False
            score.game_over()

screen.exitonclick()