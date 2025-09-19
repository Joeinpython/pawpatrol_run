# the target is to set a race for pawpatrol character by turtle graphics
from turtle import Turtle, Screen 
import random
import time

def on_click():
    homepage_.speed(0)
    homepage_.penup()
    homepage_.setpos(2000,2000)

home_page=Screen()
home_page.addshape("homepage.gif")
homepage_=Turtle(shape="homepage.gif")


is_race_on=True
screen=Screen()
screen.setup(width=1200, height=700)
screen.tracer(0)
user_bet=screen.textinput(title="Make your bet", prompt="which one in paw patrol will win the race? Enter a name")
pawname=["chase","zuma","rocky","rumble","marshall","skye","turtle"]
paw_name=["chase.gif","zuma.gif","rocky.gif","rumble.gif","marshall.gif","skye.gif","turtle"]
all_pawpatrol=[]
pawpatrol=[]

home_page.onscreenclick(on_click())
# homepage_.onclick(on_click())


for _ in range(6):
    screen.addshape(paw_name[_])

for turtle_no in range(7):
    paw_patrol=Turtle(shape=paw_name[turtle_no])
    paw_patrol.shapesize(3,3,1)
    paw_patrol.penup()
    paw_patrol.goto(x=520,y=-310+turtle_no*100)

    paw_patrol.color("red")
    pawpatrol.append(paw_patrol)

pawpatrol[6].setheading(180)

while is_race_on:
    dummy=-1
    for i in pawpatrol[0:6]:
        dummy += 1
        if i.xcor()<=-550:
            is_race_on=False
            winner=pawname[dummy]
            if winner== user_bet:
                print (f"You've won the game!! {winner} is the winner")
            else:
                print(f"You loose the game!! {winner} is the winner")    

        rand_distance=random.randint(0,30)
        i.backward(rand_distance)
    if pawpatrol[6].xcor()<=-550:
            is_race_on=False
            winner="turtle"
            if winner=="turtle":
                print (f"You've won the game!! {winner} is the winner")
            else:
                print(f"You loose the game!! {winner} is the winner")    

    rand_distance=random.randint(0,30)
    pawpatrol[6].forward(rand_distance)
    screen.update()


    time.sleep(0.2)  # 控制遊戲速度

screen.exitonclick()