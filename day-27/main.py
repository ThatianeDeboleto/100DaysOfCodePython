from tkinter import *
#bibioteca padrao da linguagem de py

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#acrescentar a janela para edicao e poder diminuir ou aumentar a janela


window = Tk()
window.title("Meu primeiro programa GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label - colocar componentes na janela
my_label = Label(text="Eu sou Label", font=("Arial", 24, "italic"))
#centralizar
my_label.pack()
#tim.write()
my_label.config(text="Novo texto")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Botoes posicoes
button = Button(text="Clique em mim", command=button_clicked)
button.grid(column=1, row=0)

new_button = Button(text="Novo botão")
new_button.grid(column=1, row=2)

#Escrever apertar / posicao
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=1)
#O que torna possivel ver e editar
window.mainloop()
