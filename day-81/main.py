from time import sleep

#Codigo Morse O Código Morse é um sistema telegráfico que pode ser utilizado em várias línguas.
# É composto por pontos, traços e espaços que representam letras, números e sinais de pontuação e foi utilizado por
# governos e por militares.
#Esse sistema permite a transmissão de mensagens à distância, por fio ou por rádio, através de sons de curta e
# de longa duração.


print('-' * 40)
print('Tradutor de texto para código Morse')
print('por @ThatianeDeboleto')
print('-' * 40)


alfabetomorse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
           'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
           'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
           'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
           'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
           'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
           'Y': '-.--', 'Z': '--..',

           '0': '-----', '1': '.----', '2': '..---', '3': '...--',
           '4': '....-', '5': '.....', '6': '-....', '7': '--...',
           '8': '---..', '9': '----.', ' ': '\n'
                 }
option = '1'

while option == '1':
    try:
        text = input('Digite aqui o texto: ').upper()

        morse = ' '

        for char in text:
            sleep(1)
            morse = alfabetomorse[char]
            if char != " ":
                print("{} = {}".format(char, morse))
            else:
                print(morse)

        sleep(0.5)

        print('Tradução completa!')
        print("Deseja traduzir outro texto?")
        option = input("1. Sim\n2. Não\n=> ")

    except KeyError as e:
        char_error = str(e).replace("\'", '')
        print('{} = Caractere não reconhecido'.format(char_error))
        print('Tente novamente!')
    except KeyboardInterrupt:
        option = '2'
        print('')

print("Você decidiu sair!")