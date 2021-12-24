from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# import pyperclip
# pyperclip recurso instalar para salvando emails - copia
# ---------------------------- gerador de senhas ------------------------------- #

# Projeto Gerador de Senha
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SALVAR SENHA ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_date = {website: {
        "email": email,
        "password": password,
    }
    }

    # Informacao pop up
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Certifique-se de que não deixou nenhum campo vazio.")
    else:
        try:
            # JSON arquivo com série de dados estruturados em forma de texto -transferir informações sistema
            with open("data.json", "r") as data_file:
                # guardar dados
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json") as data_file:
                # carregar dados
                json.dump(new_date, data_file, indent=4)

        else:
            # atualizar dados
            data.update(new_date)

            with open("data.json", "w") as data_file:
                # salvar dados
                json.dump(data, data_file, indent=4)
        finally:
            # data_file.write(f"{website} | {email} | {password}\n")
            # permitir que apague dados digitados na tela // clear apos gerar senha
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- fim senha/dicionario/busca json ------------------------------- #
def find_password():
    website = website_entry.get()
    with open("data.json") as data_file:
        data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nSenha:{password}")


# ---------------------------- CONFIGURAÇÃO DE IU ------------------------------- #
# posicao da imagem
window = Tk()
window.title("Gerenciador de senhas")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Etiquetas
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Usuário:")
email_label.grid(row=2, column=0)
password_label = Label(text="Senha/Password:")
password_label.grid(row=3, column=0)

# Entradas
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
# permitir que digite na tela
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=3)
# caso goste de deixar um email como Preenchido
email_entry.insert(0, "deboletothatiane@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Botoes adicionar a tela de inicio
search_button = Button(text="Pesquisar", width=10, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Gerador de Senha", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
