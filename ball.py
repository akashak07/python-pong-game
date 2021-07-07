from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove=10
        self.ymove=10
        self.ballspeed=0.10
        # self.shapesize(1,1)

    def move(self):
        self.newx=self.xcor()+self.xmove
        self.newy=self.ycor()+self.ymove
        self.goto(x=self.newx,y=self.newy)
    def ybounce(self):
        self.ymove *= -1
    def xbounce(self):
        self.xmove *= -1
        self.ballspeed * 0.9

    def reset(self):
        self.goto(x=0,y=0)
        self.ballspeed=0.10
        self.xbounce()


