from turtle import Turtle
import random

COLORS = ["green", "blue", "red", "pink", "purple"]


class CarManager:
    def __init__(self):
        self.cars = []
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))

