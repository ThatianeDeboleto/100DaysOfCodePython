#For Loop with Lists
frutas = ["Maça", "Uva", "Perá"]
for fruta in frutas:
  print(fruta)
  print(fruta + " cortada")

#For Loop with Range
#range gerador de sequencias de numeros
for numero in range(1, 20):
    print(numero)

for numero in range(1, 100):
  print(numero)

for numero in range(1, 101):
  print(numero)

for numero in range(1, 11, 3):
  print(numero)

#Calculando a soma de todos os números de 1 a 100.
total = 0
for numero in range(1, 101):
  total += numero
print(total)
