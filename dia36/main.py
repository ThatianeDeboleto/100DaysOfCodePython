import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "+12079528447"
VERIFIED_NUMBER = "+5511964674101"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
#https://newsapi.org/docs/endpoints/everything
STOCK_API_KEY = "YRPFECPOHKLOJA5H"
#https://newsapi.org/register/success
NEWS_API_KEY = "956d4bfaeb5c41c99de82cb7db57aa0d"
TWILIO_SID = "0724ddf0effb330060f303ed3970ac6c"
TWILIO_AUTH_TOKEN = "ACc3a6f5cdae61c6a6e3dfb29e19dd11bd"
#dicionario em py para chamar as funcionalidades
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
#dar toda a lista como dicionario FORNECE COMO CHAVE
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
#DIA 26-relembrar LISTAS
data_list = [value for (key, value) in data.items()]
#obter ontem dados
yesterday_data = data_list[0]
#fechamento ontem dados - chave Particular
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#Obtenha o preço de fechamento das ações anteontem
#1 o primeiro dia 0 anteontem seria 1 pois recua conforme a passagem do primeiro dia deteminado
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#Encontre a diferença positiva entre 1 e 2. por ex. 40 - 20 = -20, mas a diferença positiva é 20:
# https://www.w3schools.com/python/ref_func_abs.asp
#para retirar o erro float e parenteses nas funcoes // funcao abs para positivar o valor-diferenca positiva
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
#para que seja verdade deve ser maior que 0 sendo este um saldo positivo
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#Calcule a diferença percentual no preço entre o preço de fechamento ontem e o preço de fechamento anteontem.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

#Em vez de imprimir ("Obter notícias"), use a API de notícias para obter artigos relacionados à COMPANY_NAME.
#Se a porcentagem de diferença for maior que 5, imprima ("Receba notícias").
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
#ARTICLES LISTA DICIONARIO
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)

    #Crie uma nova lista do título e da descrição dos 3 primeiros artigos usando a compreensão de lista.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    #Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.message.create(
            body=article,
            from_="+12079528447",
            to="+5511964674101"
        )
