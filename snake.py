from turtle import Turtle


POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
    def create_snake(self):
            for pos in POSITIONS:
                self.add_block(pos)

    def add_block(self,position):

        turtle = Turtle(shape='square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(position)
        self.snake.append(turtle)

    def extend(self):
        self.add_block(self.snake[-1].position())

    def move(self):
            for block in range(len(self.snake)-1, 0 ,-1):
                new_x = self.snake[block - 1].xcor()
                new_y = self.snake[block - 1].ycor()
                self.snake[block].goto(new_x,new_y)
            self.snake[0].forward(20)

    def reset_snake(self):
        for i in self.snake:
            i.goto(1000,500)
        self.snake.clear()
        self.create_snake()






    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)
    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)
    def left(self):
        if self.snake[0].heading()!= RIGHT:
            self.snake[0].setheading(LEFT)
    def right(self):
        if self.snake[0].heading()!= LEFT:
            self.snake[0].setheading(RIGHT)






    def game_over(self):
        turtle = Turtle()
        turtle.penup()
        turtle.color('white')
        turtle.goto(-60,0)

