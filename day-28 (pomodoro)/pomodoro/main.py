import math
from tkinter import *
# ---------------------------- Contar o tempo ------------------------------- #
PINK = "#F7DBF0"
RED = "#e7305b"
MAROON = "#FF0000"
TEAL = "#CDF0EA"
FONT_NAME = "FreeMono"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None

# ---------------------------- Resetar tempo ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Pomodoro")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- Mecanismo Tempo ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Pausa", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Pausa", fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Pomodoro", fg=MAROON)


# ------------------------- Mecanismo de contagem regressiva ------------------------------- #
def count_down(count):
# divide / e arredonda para o valor de leitura compreensivo ao usuario %
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
# Configuracao para aparecer 25:00 , 00:00 por exemplo
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- GUI interfaces gráficas do usuário ---------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=TEAL)


title_label = Label(text="Pomodoro", fg=MAROON, bg=TEAL, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# ----------------------- Canvas Imagem ---------------------------------- #
# BG mudar a cor ao redor da imagem para a mesma do fundo da tela POMODORO
canvas = Canvas(width=200, height=224, bg=TEAL, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Começar", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reiniciar", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=MAROON, bg=TEAL)
check_marks.grid(column=1, row=3)

window.mainloop()











