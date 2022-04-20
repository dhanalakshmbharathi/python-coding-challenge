
from turtle import Screen
from food import Food
import time
from score_board import ScoreBoard
from snake import Snake
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
score=ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        score.increase_score()
    #detect collision with wall
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        score.game_over()
        game_is_on=False
    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()
screen.exitonclick()
