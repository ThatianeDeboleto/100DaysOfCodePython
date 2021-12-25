import tkinter as tk

win = tk.Tk()
win.title("App de escrita de texto desaparecendo")

textbox = tk.Text(height=10, width=100)
textbox.insert(tk.END, "Bem vindo a app de escrita")
textbox.pack()

# This is for demonstration purposes
tk.Text(height=10, width=10).pack()


def default(event):
    current = textbox.get("1.0", tk.END)
    if current == "Padrão\n":
        textbox.delete("1.0", tk.END)
    elif current == "\n":
        textbox.insert("1.0", "Padrão")


textbox.bind("<FocusIn>", default)
textbox.bind("<FocusOut>", default)

tk.mainloop()
