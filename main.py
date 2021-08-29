from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
horizontal_padding = 20
WIDTH = 500
HEIGHT = 400
vertical_padding = HEIGHT//7
screen.setup(width=WIDTH, height=HEIGHT)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-(WIDTH//2) + horizontal_padding, y=-HEIGHT//2 + (index + 1) * vertical_padding)
    turtles.append(new_turtle)

# max_x = max([_.xcor() for _ in turtles])
# while max_x < WIDTH//2 - 3*horizontal_padding:
#     for each_turtle in turtles:
#         # each_turtle.speed(random.randint(0, 10))
#         each_turtle.forward(random.randint(1, 10))
#     max_x = max([_.xcor() for _ in turtles])



if user_bet:
    is_race_on = True

while is_race_on:
    for each_turtle in turtles:
        if each_turtle.xcor() > 230:
            is_race_on = False
            winning_color = each_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        each_turtle.forward(rand_distance)





#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clearthings():
#     tim.reset()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="c", fun=clearthings)
#


screen.exitonclick()
