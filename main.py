import time
from turtle import Screen
from player import Player
from car_manager import MyCarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_player = Player()
score = Scoreboard()

car_manager = MyCarManager()

screen.listen()

screen.onkey(game_player.my_move, "w")
game_is_on = True


while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move(game_player.game_level)

    if game_player.ycor() > 290:
        game_player.new_game_level()
        score.new_score(game_player.game_level)
        game_player.start()

    for my_car in car_manager.cars:
        if game_player.distance(my_car) < 15:
            score.game_over()
            game_is_on = False

screen.exitonclick()