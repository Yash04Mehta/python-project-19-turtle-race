from turtle import Turtle , Screen
import random

game_on = False

my_screen = Screen()
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
turtles = []
my_screen.setup(width=500, height=400)
x = -230
y = -100
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x, y)

    turtles.append(new_turtle)

    y += 50

user_bet = my_screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")

if user_bet:
    game_on = True

while game_on:
    for turtle in turtles:
        if turtle.xcor() > 215:
            game_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"you've Won! The winning color is {winner}.")
            else:
                print(f"you've Lost! The winning color is {winner}.")

        distance = random.randint(0,10)
        turtle.forward(distance)

'''Below is the practice for the movements of the turtle using the listener which would be helpful in other projects '''
# def move_forwards():
#     squirtle.forward(10)
#
# def move_backwards():
#     squirtle.backward(10)
#
# def turn_left():
#     squirtle.left(10)
#
# def turn_right():
#     squirtle.right(10)
#
# def clear():
#     squirtle.penup()
#     squirtle.clear()
#     squirtle.home()
#     squirtle.pendown()
#
# my_screen.listen()
# my_screen.onkey(key="w", fun=move_forwards)
# my_screen.onkey(key="s", fun=move_backwards)
# my_screen.onkey(key="a", fun=turn_left)
# my_screen.onkey(key="d", fun=turn_right)
# my_screen.onkey(key="c", fun=clear)
my_screen.exitonclick()
