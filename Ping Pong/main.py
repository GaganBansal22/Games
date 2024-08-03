from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(800,500)
screen.title("Ping Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if(ball.ycor()>=240 or ball.ycor()<=-240):
        ball.bounce_y()

    if((ball.xcor()>320 and ball.distance(r_paddle)<50) or (ball.xcor()<-320 and ball.distance(l_paddle)<50)):
        ball.bounce_x()
        ball.ball_speed*=0.9

    if ball.xcor()>=380:
        ball.reset_pos()
        scoreboard.point(0)

    if ball.xcor()<=-380:
        ball.reset_pos()
        scoreboard.point(1)

    if scoreboard.l_score==5 or scoreboard.r_score==5:
        game_is_on=False

screen.exitonclick()