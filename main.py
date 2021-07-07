from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score
sc=Screen()
sc.setup(width=800,height=600)
sc.bgcolor("black")
sc.tracer(0)

rpad=Paddle(350,0)
lpad=Paddle(-350,0)

ball=Ball()

score=Score()

sc.listen()
sc.onkey(fun=rpad.up,key="Up")
sc.onkey(fun=rpad.down,key="Down")
sc.onkey(fun=lpad.up,key="w")
sc.onkey(fun=lpad.down,key="s")
gameon=True
while gameon:
    #sleep is used to update the screen for the ball movement
    time.sleep(ball.ballspeed)
    sc.update()
    ball.move()
    #detecting collision with the up and down wall
    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.ybounce()
    #detecting collision with the ball and paddle
    if ball.distance(rpad)<50 and ball.xcor()>330 or ball.distance(lpad)<50 and ball.xcor()<-330:
        ball.xbounce()
    if ball.xcor() > 380:
        ball.reset()
        score.scorey()
    if ball.xcor()<-380:
        ball.reset()
        score.scorex()


sc.exitonclick()