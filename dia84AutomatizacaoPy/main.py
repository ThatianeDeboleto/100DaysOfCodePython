from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import filedialog

'''PIL ou Biblioteca de Imagens do Python é um pacote que expõe muitas funções para 
manipular imagens a partir de um script Python.
USO PILLEW - Sequencia para biblioteca atualizada Py'''

def upload_image():
    global img
    filepath = filedialog.askopenfilename(
        initialdir="/", title="Selecionar o arquivo", filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
    img = Image.open(filepath)
    label_width = label.winfo_width()
    label_height = label.winfo_height()
    maxsize = (label_width, label_height)
    resized_original = img.resize(maxsize, Image.ANTIALIAS)
    ph_original = ImageTk.PhotoImage(img)
    label['image'] = ph_original
    Image.show()


def watermarking():
    draw = ImageDraw.Draw(img)
    text = entry.get()
    font = ImageFont.truetype('arial.ttf', 48)
    textwidth, textheight = draw.textsize(text, font)

    # calcular coordenada x e y da imagem
    margin = img.width*0.1
    x = img.width - textwidth - margin
    y = img.height - textheight - margin

    # desenhar marca d´agua no canto inferior direito
    draw.text((x, y), text, font=font)
    label_width = label.winfo_width()
    label_height = label.winfo_height()
    maxsize = (label_width, label_height)
    resized_after = img.resize(maxsize, Image.ANTIALIAS)
    ph = ImageTk.PhotoImage(resized_after)
    label['image'] = ph

    save_path = filedialog.asksaveasfilename(
        filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
    img.save(f'{save_path}.jpg')


root = Tk()
root.title("Textos em suas imagens")
root.minsize(width=600, height=500)

frame = Frame(root, bg='#406882', bd=0.05)
frame.place(relx=0.1, rely=0.10, relwidth=0.8, relheight=0.8)

upload_button = Button(frame, text='Upload imagem', command=upload_image)
upload_button.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.07)

entry_label = Label(frame, text='Insira um texto', bg='#1A374D')
entry_label.place(relx=0.1, rely=0.21, relwidth=0.28, relheight=0.07)
entry = Entry(frame)
entry.place(relx=0.4, rely=0.21, relwidth=0.5, relheight=0.07)

watermark_button = Button(frame, text='Adicionar texto a imagem', command=watermarking)
watermark_button.place(relx=0.1, rely=0.32, relwidth=0.8, relheight=0.07)

label = Label(frame)
label.place(relx=0.1, rely=0.42, relwidth=0.8, relheight=0.46)

quit_button = Button(frame, text='sair', command=root.destroy)
quit_button.place(relx=0.8, rely=0.9, relwidth=0.1, relheight=0.05)


root.mainloop()
