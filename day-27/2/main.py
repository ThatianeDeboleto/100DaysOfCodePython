from tkinter import *

window = Tk()
window.title("conversor de milhas para quilômetro")
window.config(pandx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(colum=1, row=8)


miles_label = Label(text="Milhas")
miles_label.grid(colum=2, row=8)

is_equal_label = Label(text="é igual a")
is_equal_label.grid(colum=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(colum=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(colum=2, row=1)

calculate_button = Button(text="Calculo")
calculate_button.grid(colum=2, row=3)
