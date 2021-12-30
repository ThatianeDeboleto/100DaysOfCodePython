# deboletothatiane@gmail.com

import pyttsx3  # pip install pyttsx3

# ler o texto que esta guardado em um arquivo .txt / .pdf
f = open('Coloque o caminho aqui/o_pequeno_principe.pdf','r', encoding="utf8")
texto = f.read()
#iniciar a biblioteca
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')  # metodo de voz

# ver as vozes instaladas na maquina
for voice in voices:
    print(voice, voice.id)  # traz os idiomas de voz instalados em sua maquina

speaker.setProperty('voice', voices[0].id)  # define a voz padrao, no meu caso o portugues era o[0] (iniciando do zero)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate - 25)  # muda velocidade da leitura, quando menor mais lento

# escreve o texto na tela
print(texto)
# define o texto que será lido
speaker.say(texto)
# ler o texto
speaker.runAndWait()
# fecha o modo de leitura do arquivo
f.close()
