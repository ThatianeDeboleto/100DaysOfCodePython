import pyttsx3

texto = "Não desista agora, você vai chegar lá!"

speaker = pyttsx3.init()

voices = speaker.getProperty("voices")
#executar verificar vozes instalada em sua maquina PC
for voice in voices:
    print(voice, voice.id)
#após continuar e colocar numero
speaker.setProperty('voice', voices[0].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate-25) #muda velocidade da leitura, quanto menor numero mais lento

print(texto)
speaker.say(texto)
speaker.runAndWait()
