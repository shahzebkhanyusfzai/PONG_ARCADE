from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.zero = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.myscore = f"score = {self.zero}"

    def Pong_Score(self):
        self.clear()
        self.zero+=1
        self.myscore = f"score = {self.zero}"
        self.write(self.myscore, move=False, align="center", font=("Arial", 13, "bold"))

    def game_is_over(self):
        self.write("Game Over", move=False, align="center", font=("Arial", 13, "bold"))        