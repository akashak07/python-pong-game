from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.yscore = 0
        self.xscore = 0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.yscore, align="center", font=("Coutier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.xscore, align="center", font=("Coutier", 70, "normal"))

    def scorex(self):
        self.xscore += 1
        self.updatescore()

    def scorey(self):
        self.yscore += 1
        self.updatescore()

