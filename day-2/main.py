# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
IMC = float(weight) / float(height) ** 2
print(f"Seu IMC é:   {IMC}")
print("Abaixo do peso: 18,5; \n Peso normal: 18,5 - 24,9; \n Sobre peso: 24,9 - 29,9;")


#Projeto 2 dia 2
conta_restaurante = 150
numero_pessoas = 5
gorjeta = 1.12
print(round(conta_restaurante / numero_pessoas) * gorjeta)

restaurante = input("Bem vindo a calculadora de pagamentos! \nQual é o valor total da conta? $")
numero_pessoas = input("Em quantos amigos estão? ")
gorjeta = input("Qual é a taxa de gorjeta? ")

total_conta = float(restaurante)
numero_pessoas = int(numero_pessoas)
divisao_conta = total_conta / numero_pessoas
porcentagem_gorjeta = float(gorjeta) / 100

total_conta_pessoa = round(divisao_conta + (porcentagem_gorjeta * divisao_conta), 2)

print(f"O valor a ser pago, por cada um é: ${total_conta_pessoa}")
# print(total_conta_pessoa)


