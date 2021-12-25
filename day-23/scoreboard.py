from turtle import Turtle

FONT = ("Courier", 24, "normal")


# mostrar o placar
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # atributo ao level que se esta
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level 🚗: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    #  quando atropelado mostrar Game Over
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
