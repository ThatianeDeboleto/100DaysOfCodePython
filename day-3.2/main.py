# 🚨 Don't change the code below 👇
print("Bem vindo a calculadora do Amor!")
nome1 = input("Qual é seu nome? \n")
nome2 = input("Qual é o nome do seu amor? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# corda combinada
# Lower minusculo
combinacao_nomes = nome1 + nome2
menor_numero_combinacoes = combinacao_nomes.lower()

v = menor_numero_combinacoes.count("v")
e = menor_numero_combinacoes.count("e")
r = menor_numero_combinacoes.count("r")
d = menor_numero_combinacoes.count("d")
a = menor_numero_combinacoes.count("a")
d = menor_numero_combinacoes.count("d")
e = menor_numero_combinacoes.count("e")

verdade = v + e + r + d + a + d + e

a = menor_numero_combinacoes.count("a")
m = menor_numero_combinacoes.count("m")
o = menor_numero_combinacoes.count("o")
r = menor_numero_combinacoes.count("r")

amor = a + m + o + r

score_amor = str(verdade) + str(amor)

print(f"A porcentagem do amor entre vocês é de {score_amor} %")

