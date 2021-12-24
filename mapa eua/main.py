import turtle
import pandas
#ficheiro de imagem // mostrar em uma pagina de modo turtle // mostrar a imagem que esta anexada ao codigo
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
#os valores de x e y estao no csv de estados (facilitar no mapa)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
#escrever o nome do estado/dando nome errado nao decair as chances, ate que se acerte os 50 Estados
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    #quando sair a resposta, quando executar o questionario retornar
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    #Estado correto preencher o mapa / acieta letras minusculas e a primeira maiuscula
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick()