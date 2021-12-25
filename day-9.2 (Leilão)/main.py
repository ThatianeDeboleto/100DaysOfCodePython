from replit import clear
from art import logo
print(logo)

licitacao = {}
licitacao_concluida = False

def encontrar_maior_lance(lance_record):
  maior_lance = 0
  vencedor = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for lance in maior_lance:
    lance_quantia = maior_lance[lance]
    if lance_quantia > maior_lance:
      altissimo_lance = lance_quantia
      vencedor = lance
  print(f"O vencedor é {vencedor} com o lance de R${altissimo_lance}")
#repticao
while not licitacao_concluida:
  nome = input("Qual é seu nome?: ")
  valor = int(input("Quanto quer utilizar no seu lance?: R$ "))
  licitacao[nome] = valor
  deve_continuar = input("Você quer continuar com os lances? Digite 'sim' ou 'não'.\n")
  if deve_continuar == "não":
    bidding_finished = True
    encontrar_maior_lance(licitacao)
  elif deve_continuar == "sim":
    clear()