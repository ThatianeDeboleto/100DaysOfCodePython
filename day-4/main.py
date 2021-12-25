#projeto1
# Split string method
nomes_string = input("Qual cartão de crédito será selecionado - até 7 pessoas: ")
nomes = nomes_string.split(", ")
# 🚨 Don't change the code above 👆
# split permite escrever em cordao em componentes separados.
#Write your code below this line 👇
numero_itens = len(nomes)

import random
random_chances = random.randint(0, numero_itens - 1)
quem_pagara = nomes[random_chances]

print(quem_pagara + " é você quem pagará a refeição hoje!")
#projeto2
# 🚨 Don't change the code below 👇
row1 = ["🥰", "🙁", "😖"]
row2 = ["😬", "😔", "🤧"]
row3 = ["🥳", "🤓", "😮"]

mapa = [row1, row2, row3]
print(f"     1     2     3\n 1{row1}\n 2{row2}\n 3{row3}")
posicao = input("Qual emoji representa seu estado de humor hoje? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(posicao[0])
vertical = int(posicao[1])

seleciona_row = mapa[vertical - 1]
seleciona_row[horizontal - 1] ="✅"





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
