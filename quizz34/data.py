import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
#excessao para erros
response.raise_for_status()
data = response.json()
#estruturar como dicionario - abrir pergunta (Verdadeiro/Falso)
question_data = data["results"]

#?amount=10&type=boolean final url
#Igneous rocks are formed by excessive heat and pressure
#Rochas ígneas são formadas por calor e pressão excessivos
#To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form.
#Para contornar as Leis de Exportação de Munições dos Estados Unidos, o criador do PGP publicou fonte livro
#In 2016, the IUCN reclassified the status of Giant Pandas from endangered to vulnerable.
#Em 2016, a IUCN reclassificou o status dos Pandas Gigantes de ameaçados para vulneráveis.
#There is a Donald Trump Board Game, which was made in 1989.
#Há um jogo de tabuleiro Donald Trump, feito em 1989.
#The National Animal of Scotland is the Unicorn.
#O Animal Nacional da Escócia é o Unicórnio.
#In the &quot;S.T.A.L.K.E.R.&quot; series, the Freedom faction wishes to destroy the supernatural area
# ...known as  &quot;the Zone&quot
#In the & quot; S.T.A.L.K.E.R. & quot; série, a facção Freedom deseja destruir a área sobrenatural
# ... conhecido como & quot; a Zona & quot
#tigers have one colour of skin despite the stripey fur
#tigers têm uma cor de pele, apesar do pelo listrado
#A scalene triangle has two sides of equal length.
#Um triângulo escaleno tem dois lados de igual comprimento.
#Vietnam&#039;s national flag is a red star in front of a yellow background
#A bandeira nacional do Vietnã é uma estrela vermelha em frente a um fundo amarelo
#The mitochondria is the powerhouse of the cell.
#a mitocôndria é a força motriz da célula.