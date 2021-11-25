FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.new_score(0)

        def new_score(self, level):
            self.penup()
            self.clear()
            self.goto(-280, 260)
            self.write("Score:", move="True", align="left", font=FONT)
            self.write(level, move="True", align="left", font=FONT)
            self.hideturtle()

        def game_over(self):
            self.goto(0, 0)
            self.write("GAME OVER!", move="True", align="center", font=FONT)

