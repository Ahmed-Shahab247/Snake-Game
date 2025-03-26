from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')



screen.tracer(0)
game_on = True
score_count = 0


snake = Snake()
food = Food()
score = Score()
screen.listen()


screen.onkey(key='Up',fun=snake.up)
screen.onkey(key='Down',fun=snake.down)
screen.onkey(key='Left',fun=snake.left)
screen.onkey(key='Right',fun=snake.right)


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    x = snake.snake[0].xcor()
    y = snake.snake[0].ycor()

    if snake.snake[0].distance(food) < 15:
        food.hideturtle()
        score.increase_score()
        snake.extend()
        food = Food()
    if x >= 300 or x <= -300 or y >= 300 or y<= -300:

        snake.reset_snake()
        score.reset()


    for i in range(1,len(snake.snake)-1):
        if snake.snake[0].distance(snake.snake[i]) <1 or snake.snake[0].distance(snake.snake[-1])<1:
            snake.reset_snake()
            score.reset()




screen.exitonclick()