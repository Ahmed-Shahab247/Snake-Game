from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.rand_x = random.randint(-230, 230)
        self.rand_y = random.randint(-230, 230)
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.goto(self.rand_x,self.rand_y)