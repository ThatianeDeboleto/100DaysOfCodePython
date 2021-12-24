import tkinter as tk
from tkinter import messagebox
from random import shuffle

#pomodoro - projeto modo turtle
PLACEHOLDER_TEXT = "digite as palavras aqui"
FONT = "Courier New", 20, "normal"
FONT_BOLD = "Courier New", 22, "bold"
ACTIVE_FONT_COLOR = '#000'
PLACEHOLDER_FONT_COLOR = '#AAA'

LETTER_COLOR_NEUTRAL = '#000'
LETTER_COLOR_SUCCESS = '#00FF00'
LETTER_COLOR_ERROR = '#FF0000'


def show_final_score():
    if is_active_timer():
        window.after_cancel(window.timer)
        window.timer = None

    timer_text = time_label.cget("text")
    seconds_left = int(timer_text.split(":")[-1][:-1])

    entered_words = entered_text.get().split()
    entered = "".join(entered_words)
    provided = "".join(sample_text)
    errors = sum([0 if provided[index] == entered[index]
                  else 1 for index in range(len(entered))])

    letters_typed = len(entered)
    letters_total = len(letters)

    if seconds_left != 60:
        char_per_min = int((letters_typed/(60 - seconds_left)) * 60)
        words_per_min = int((len(entered_words)/(60 - seconds_left)) * 60)
    else:
        char_per_min = words_per_min = 0

    message = f"Você entrou {letters_typed} letras de {letters_total} em {60 - seconds_left}s, com {errors} erros." \
              f" Isso é {char_per_min}caracteres por min, ou {words_per_min}palavras por min.\n\nQuer tentar de novo?"
    answer = messagebox.askyesno("Completo!", message)
    if not answer:
        window.destroy()
    else:
        reset_game()


def show_finished_message():
    tk.messagebox.showinfo("Completo!", "Você digitou todas as letras corretamente!")
    show_final_score()


def show_time_up_message():
    tk.messagebox.showinfo("Tempo esgotado!", "Seu tempo acabou!")
    show_final_score()


def update_matches(target, positions, source, entered):
    errors = 0
    for index, position in enumerate(positions):
        if index < len(entered):
            if source[index] == entered[index]:
                target.itemconfig(position, fill=LETTER_COLOR_SUCCESS)
            else:
                target.itemconfig(position, fill=LETTER_COLOR_ERROR)
                errors += 1
        else:
            target.itemconfig(position, fill=LETTER_COLOR_NEUTRAL)

    if len(positions) == len(entered) and errors == 0:
        show_finished_message()


def reset_text(target, positions):
    for position in positions:
        target.itemconfig(position, fill=LETTER_COLOR_NEUTRAL)


def update_timer_text():
    timer_text = time_label.cget("text")
    seconds_left = int(timer_text.split(":")[-1][:-1])
    seconds_left -= 1
    time_label.config(text=f"Tempo restante: {seconds_left}s")

    if seconds_left > 0:
        window.timer = window.after(1000, update_timer_text)
        return

    window.timer = None

    # Mostrar alerta de tempo esgotado.
    show_time_up_message()


def start_timer():
    window.timer = window.after(1000, update_timer_text)


def is_active_timer():
    return window.timer is not None


def key_pressed(var, index, mode):
    entered = entered_text.get()
    if entered == "" or entered == PLACEHOLDER_TEXT:
        reset_text(canvas, letters)
        return True

    if not is_active_timer():
        start_timer()

    update_matches(canvas, letters, "".join(
        sample_text), "".join(entered.split()))
    return True


def display_text(target, word_list):
    positions = []
    letter_count = 0
    row_count = 0
    for word in word_list:
        # If the word won't fit on a line, start a new one.
        if letter_count + len(word) > 36:
            letter_count = 0
            row_count += 1
            if row_count > 2:
                break

        # Escreva cada caractere na tela.
        for char in word:
            x_coord = 16 + letter_count * 14
            y_coord = 16 + row_count * 45
            letter = target.create_text(
                x_coord, y_coord,
                fill=LETTER_COLOR_NEUTRAL, font=FONT_BOLD,
                text=char, anchor="nw"
            )
            positions.append(letter)
            letter_count += 1

        # Adicione um espaço entre as palavras.
        letter_count += 1

        # Após 36 caracteres, incluindo espaços, comece uma nova linha.
        if letter_count > 36:
            letter_count = 0
            row_count += 1

        # Exiba apenas três linhas.
        if row_count > 2:
            break

    return positions


def generate_sample_text():
    with open("./data/word_list.txt", "r") as file:
        words = [line.rstrip() for line in file.readlines()]
        shuffle(words)
        return words[0:100]


def entry_has_focus(event):
    text = entry_box.get()
    if text == PLACEHOLDER_TEXT:
        entry_box.delete(0, tk.END)
    entry_box.config(fg=ACTIVE_FONT_COLOR)


def entry_lost_focus(event):
    text = entry_box.get()
    if text == "":
        entry_box.insert(0, PLACEHOLDER_TEXT)
    entry_box.config(fg=PLACEHOLDER_FONT_COLOR)
    pass


def reset_game():
    # Obtenha um novo texto de amostra.
    global sample_text, letters
    sample_text = generate_sample_text()

    #Remova as letras existentes e adicione as novas.
    for letter in letters:
        canvas.delete(letter)
    letters = display_text(canvas, sample_text)

    # Esvazie a caixa de entrada.
    entry_box.delete(0, tk.END)

    # Redefina o rótulo do cronômetro
    time_label.config(text="Tempo restante: 60s")


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Minuto extra")
    window.configure(background='#F8F8F0', padx=16, pady=16)
    window.resizable = False, False
    window.timer = None

    top_frame = tk.Frame(window)
    top_frame.config(
        background='#EEEEEE',
        highlightbackground="#000",
        highlightcolor="#000",
        highlightthickness="2",
        bd=0
    )
    top_frame.grid(row=0, column=0, sticky="ew")

    time_label = tk.Label(top_frame, text="Tempo restante: 60s")
    time_label.grid(row=0, column=0)

    canvas = tk.Canvas(window)
    canvas.config(
        background="#FFFFFF",
        width=600,
        height=150,
        highlightbackground="#000",
        highlightcolor="#000",
        highlightthickness="2",
        bd=0
    )
    canvas.grid(row=1, column=0, sticky="ew")

    sample_text = generate_sample_text()
    letters = display_text(canvas, sample_text)

    bottom_frame = tk.Frame(window)
    bottom_frame.config(
        background='#EEEEEE',
        highlightbackground="#000",
        highlightcolor="#000",
        highlightthickness="2",
        bd=0
    )
    bottom_frame.columnconfigure(0, weight=1)
    bottom_frame.config(padx=8, pady=8)
    bottom_frame.grid(row=2, column=0, sticky="ew")

    entered_text = tk.StringVar()
    entered_text.trace_add("write", key_pressed)

    entry_box = tk.Entry(bottom_frame, textvariable=entered_text)
    entry_box.config(background='#EEEEEE',
                     fg=PLACEHOLDER_FONT_COLOR, font=FONT, relief=tk.FLAT)
    entry_box.grid(row=0, column=0, sticky="ew")
    entry_box.insert(0, PLACEHOLDER_TEXT)

    # No foco, remova o espaço reservado.
    entry_box.bind("<FocusIn>", entry_has_focus)

    # Ao perder o foco, restaure o marcador de posição se estiver vazio
    entry_box.bind("<FocusOut>", entry_lost_focus)

    window.mainloop()

