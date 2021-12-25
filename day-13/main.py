def minha_funcao():
  for i in range(1, 21):
    if i == 20:
      print("Você entendeu!")
minha_funcao()

# Reproduzir bug
from random import randint
dadas_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dados_num = randint(0, 5)
print(dadas_imgs[dados_num])

# Play Computador
ano = int(input("Qual ano do seu nascimento?"))
if ano > 1980 and ano < 1994:
  print("Você é da geração milenium.")
elif ano >= 1994:
  print("Você é da geração Z.")

# Fixos erros
idade = int(input("Qual é sua idade?"))
if idade > 18:
  print(f"Você pode dirigir com {idade} anos.")

#Print
paginas = 0
mundo_page = 0
paginas = int(input("Numero de paginas: "))
mundo_page = int(input("Numero de palavras por pagina: "))
total_mundos = paginas * mundo_page
print(f"paginas = {paginas}")
print(f"número de palavras = {mundo_page}")
print(total_mundos)

#Use a Debugger
def mutante(a_lista):
    b_lista = []
    for item in a_lista:
        novo_item = item * 2
        b_lista.append(novo_item)
    print(b_lista)

mutante([1, 2, 3, 5, 8, 13])



