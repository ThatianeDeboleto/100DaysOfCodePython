from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
#import pyperclip
#pyperclip recurso instalar para salvando emails - copia
# ---------------------------- gerador de senhas ------------------------------- #

#Projeto Gerador de Senha
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    #pyperclip.copy(password)

# ---------------------------- SALVAR SENHA ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
# Informacao pop up
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Certifique-se de que não deixou nenhum campo vazio.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Estes são os detalhes inseridos: \nEmail: {email} "
                                                      f"\nSenha: {password} \nGostaria de salvar?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                #permitir que apague dados digitados na tela // clear apos gerar senha
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- CONFIGURAÇÃO DE IU ------------------------------- #
#posicao da imagem
window = Tk()
window.title("Gerenciador de senhas")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Etiquetas
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Usuário:")
email_label.grid(row=2, column=0)
password_label = Label(text="Senha/Password:")
password_label.grid(row=3, column=0)

#Entradas
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=3)
#permitir que digite na tela
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=3)
#caso goste de deixar um email como Preenchido
email_entry.insert(0, "")
password_entry = Entry(width=19)
password_entry.grid(row=3, column=1)

# Botoes adicionar a tela de inicio
generate_password_button = Button(text="Gerador de Senha", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=31, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()