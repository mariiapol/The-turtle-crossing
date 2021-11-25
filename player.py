STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_position()
        self.game_level = 0

    def starting_position(self):
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def my_move(self):
        self.forward(MOVE_DISTANCE)

    def start(self):
        self.reset()
        self.starting_position()

    def new_game_level(self):
        self.game_level += 1






