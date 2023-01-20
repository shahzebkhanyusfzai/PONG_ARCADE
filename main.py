import turtle
from slider import Slider
from ball import Ball
import time
from score import Score
screen = turtle.Screen()
MyBall = Ball()
RightScore = Score()
LeftScore = Score()
myscore = Score()
RightScore.goto(-100,280)
LeftScore.goto(100,280)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
RightSlider = Slider()
LeftSlider = Slider()
RightSlider.goto(-280,0)
LeftSlider.goto(280,0)
screen.update()
screen.listen()
screen.onkey(RightSlider.up,"Up")   
screen.onkey(RightSlider.down,"Down")
screen.onkey(LeftSlider.up,"q")   
screen.onkey(LeftSlider.down,"w")

game_is_on = True
while game_is_on:
    MyBall.ballmove()
    screen.update()
    time.sleep(0.1)
    if RightSlider.distance(MyBall)<30 :
        MyBall.sliderbounce()
        RightScore.Pong_Score()

    if LeftSlider.distance(MyBall)<30:
        MyBall.sliderbounce()
        LeftScore.Pong_Score()

    if MyBall.ycor()>280 or MyBall.ycor()<-280:
        MyBall.groundbounce() 

    if MyBall.xcor()>300 or MyBall.xcor()<-300 or MyBall.ycor()>300 or MyBall.ycor()<-300:
        game_is_on = False
        myscore.game_is_over()
    # if LeftSlider.distance(MyBall)<15:
    #     MyBall.ballbounce()
screen.exitonclick()