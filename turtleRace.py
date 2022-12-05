from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet",
                            prompt="which turtle will win the race? Enter a color")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cordi= 0
all_turtles = []
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_cordi - 70)
    y_cordi += 30
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # the width is 500 and the turtle shape is 40 => 250 - (40/2) = 230
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()