from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.right(random.randint(0,45))
        self.x_move = 7
        self.y_move = 7    
        
    def ballmove(self):
        self.new_x = self.xcor() + self.x_move
        self.new_y = self.ycor() + self.y_move
        self.goto(self.new_x,self.new_y)

    def sliderbounce(self):
        self.x_move *=-1

    def groundbounce(self):
        self.y_move *=-1