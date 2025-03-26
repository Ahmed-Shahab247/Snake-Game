from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt", mode ="r") as data:
                high_score = int(data.read())

        self.high_score = high_score

        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updated_score()


    def updated_score(self):

        self.clear()
        self.write(f"Your current score :{self.score}  Your highest score {self.high_score}"
                   ,align='center',font=('Courier', 13, 'normal'))


    def increase_score(self):
        self.score += 1
        self.updated_score()


    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score

            with open("high_score.txt", mode ="w") as highest:
                highest.write(f"{self.high_score}")

        self.score = 0
        self.updated_score()

