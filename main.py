from turtle import Screen
from player import Player
from car_manager import CarManager
import time

screen = Screen()
#Setting up screen size
screen.setup(width=600, height=600)
#screen.tracer(0)

#listen to the user input
screen.listen()
player = Player()
car_manager = CarManager()
#move the trutle up
screen.onkey(player.move_up, "Up")

is_game_on = False

while is_game_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
