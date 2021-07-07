from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xc,yc):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(x=xc,y=yc)

    def up(self):
        self.newy=self.ycor()
        self.x=self.xcor()
        self.goto(x=self.x,y=self.newy+30)
    def down(self):
        self.newy = self.ycor()
        self.x = self.xcor()
        self.goto(x=self.x, y=self.newy - 30)

