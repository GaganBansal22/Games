from turtle import Turtle
import random

class Cars:
    def __init__(self):
        self.segments=[]
        self.colors=["red","yellow","green","blue","purple"]
        self.car_speed=5

    def make_car(self):
        choice=random.randint(1,6)
        if choice==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.pu()
            new_car.color(random.choice(self.colors))
            new_car.goto(400,random.randint(-200,200))
            self.segments.append(new_car)
    
    def move_cars(self):
        for car in self.segments:
            car.bk(self.car_speed)