import turtle,pandas

screen=turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("Udemy/Python/Games/US States Game/blank_states_img.gif")
turtle.shape("Udemy/Python/Games/US States Game/blank_states_img.gif")

score=0
data=pandas.read_csv("Udemy/Python/Games/US States Game/50_states.csv")
names=data.state.to_list()
t=turtle.Turtle()
t.pu()
t.hideturtle()
t.speed("fastest")

game_is_on=True
while game_is_on:
    guess=screen.textinput(f"{score}/50 states correct","What's another state?")
    guess=guess.title()
    if guess in names:
        score+=1
        names.pop(names.index(guess))
        t.goto(int(data[data.state==guess].x),int(data[data.state==guess].y))
        t.write(guess)
        # t.goto(0,0)
        if score==50:
            game_is_on=False
    if guess=="Exit":
        game_is_on=False

screen.exitonclick()