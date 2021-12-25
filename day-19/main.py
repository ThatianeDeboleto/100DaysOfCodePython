#timmy verde tommy purpura
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Em quem vai apostar?", prompt="Qual tartaruga vence a corrida? Escolha uma cor: ")
cores = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_tim = Turtle(shape="tartaruga")
    new_tim.penup()
    new_tim.cores(cores[turtle_index])
    new_tim.goto(x=-238, y=y_positions[turtle_index])
    all_turtle.append(new_tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_cores = turtle.pencores()
            if winning_cores == user_bet:
                print(f"Você ganhou! A vencedora é {winning_cores} ")
            else:
                print(f"Você perdeu, a cor vencedora é {winning_cores}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

