from tkinter import *
import requests
#ADD CORES AO FUNDO DO TK BOTAO CANVAS
BACKGROUND_COLOR = "#9D5C0D"
#rotacao de frases da api utilizando json
#API é um conjunto de definições e protocolos usado no desenvolvimento e na integração de software de aplicações.
#JSON é basicamente um formato leve de troca de informações/dados entre sistemas
def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    #configuracao do texto no codigo
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 200, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="black")
#bg add cor
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)
#funcao do botao, posicao, cor de fundo, uso da imagem png
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bg=BACKGROUND_COLOR)
kanye_button.grid(row=1, column=0)

window.mainloop()