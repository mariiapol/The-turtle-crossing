from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class MyCarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        i = random.randint(0, 4)
        if i == 1:
            my_car = Turtle("square")
            my_car.shapesize(1, 2)
            my_car.color(random.choice(COLORS))
            my_car.penup()
            my_car.goto(290, random.randint(-290, 290))
            self.cars.append(my_car)

    def move(self, level):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + level*MOVE_INCREMENT)



