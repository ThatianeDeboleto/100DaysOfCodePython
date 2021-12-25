from random import randint
from art import logo

NIVEL_FACIL = 10
NIVEL_DIFICIL = 5


# Quantas chances ainda existem!!!!
def check_respostas(acho, resposta, vezes):
    if acho > resposta:
        print("Muito alto.")
        return vezes - 1
    elif acho < resposta:
        print("Muito baixo.")
        return vezes - 1
    else:
        print(f"Você conseguiu! A resposta certa é: {resposta}.")


# Nivel de dificuldade
def set_dificuldade():
    level = input("Escolha qual nível de dificuldade quer jogar. Digite 'facil: ou 'dificil'. ")
    if level == "facil":
        return NIVEL_FACIL
    elif level == "dificil":
        return NIVEL_DIFICIL
    else:
        print("Digite apenas 'facil' ou 'dificil'.")
        game()


# Inicio do jogo
def game():
    print(logo)
    # Chances de escolha de 1 a 100.
    print("Bem vindo ao Mentalista!")
    print("Eu estou pensando em um número entre 1 e 100.")
    resposta = randint(1, 100)

    # Quantas chances existem
    vezes = set_dificuldade()
    acho = 0
    while acho != resposta:
        print(f"Você tem {vezes} tentativas para descobrir o número.")

        acho = int(input("Adivinhe: "))

        vezes = check_respostas(acho, resposta, vezes)
        if vezes == 0:
            print(f"Você não tem mais chances. Você perdeu. A resposta correta é {resposta}")
            return
        elif acho != resposta:

            print("Adivinhe de novo.")

        '''resolucao do print no inicio!!!'''
        # print(f"Pssst, a resposta correta é {resposta}")


game()


