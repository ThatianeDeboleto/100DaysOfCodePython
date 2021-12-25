from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# A tartaruga na tela (velocidade)
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # mover a tartaruga para cima - agora ela sobe
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    #  tartaruga voltar a posicao inicial apos atravessar a rua
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    #   passar fases
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
