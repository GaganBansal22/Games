from turtle import Screen
from scoreboard import Scoreboard
from cars import Cars
from player import Player
import time

screen=Screen()
screen.bgcolor("white")
screen.setup(800,500)
screen.title("Turtle Crossing Game")
screen.tracer(0)

cars=Cars()
player=Player()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(player.move_up,"Up")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.make_car()
    cars.move_cars()
    if(player.ycor()>=210):
        player.finish()
        cars.car_speed+=10
        scoreboard.point()
    for car in cars.segments:
        if car.distance(player)<=20:
            game_is_on=False
            scoreboard.game_over()


screen.exitonclick()