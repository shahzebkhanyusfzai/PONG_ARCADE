from turtle import Turtle
from ball import Ball
class Slider(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(4,1)

    def up(self):
        # self.forward(10)
        self.sety(self.ycor()+30)
    def down(self):
        # self.backward(10)
        self.sety(self.ycor()-30)
