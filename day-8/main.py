alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direcionar = input("Digite 'codificar' para criptografar, digite 'decodificar' para descriptografar:\n")
texto = input("Digite sua mensagem:\n").lower()
mudar = int(input("Digite o número:\n"))

def caesar(texto_inicial, quantidade_de_deslocamento, direcao_da_cifra):
  fim_texto = ""
  if direcao_da_cifra == "decode":
      quantidade_de_deslocamento *= -1
    #LOOP For / INDEX = indice
  for letras in texto_inicial:
    posicao = alfabeto.index(letras)
    nova_posicao = posicao + quantidade_de_deslocamento
    fim_texto += alfabeto[nova_posicao]
  print(f"Aqui está o {direcao_da_cifra} resultado: {fim_texto}")

caesar.str('texto', 'deslocamento', 'cifra')
