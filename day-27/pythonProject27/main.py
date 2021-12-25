import tkinter

window = tkinter.Tk()
window.title("Conversor de milhas para quilometro.")
window.minsize(width=400, height=200)
window.config(padx=80, pady=50)

label1 = tkinter.Label(text="Milhas")
label1.grid(column=2, row=0)

label2 = tkinter.Label(text="É igual a:")
label2.grid(column=0, row=1)

label3 = tkinter.Label(text="Km")
label3.grid(column=2, row=1)

label4 = tkinter.Label(text=0)
label4.grid(column=1, row=1)


# CALCULO PARA CONVERSAO
def calc():
    miles = int(entry.get())
    km = round(miles * 1.609)
    label4.config(text=f"{km}")


# BOTAO ADICIONAL
button = tkinter.Button(text="calcular", command=calc)
button.grid(column=1, row=2)

# POSICAO
entry = tkinter.Entry()
entry.grid(column=1, row=0)

window.mainloop()
