
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
#https://api.openweathermap.org/data/2.5/weather?q=Campinas,BR&appid=2d89dd12121df826d86dad8103fba406
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("2d89dd12121df826d86dad8103fba406")
account_sid = "drathatianenimtzz@gmail.com"
auth_token = os.environ.get("AUTH_TOKEN")
#exclude parametro do proprio site
parametros_do_tempo = {
    "lat": "-22.907370",
    "lon": "-47.062901",
    "appid": "2d89dd12121df826d86dad8103fba406",
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parametros_do_tempo)
#print(response.json()) - mostra no console parametros
response.raise_for_status()
weather_data = response.json()
#lista de dias e horas
weather_slice = weather_data["hourly"][:12]
#print(weather_slice)
will_rain = False
#atualizacao de hora em hora
for hour_data in weather_slice:
    #print(hour_data["weather"])
    #adicionar o horario de interesse
    condition_code = hour_data["weather"][0]["id"]
    #condicao inferior a 700 levar guarda chuva
    if int(condition_code) < 700:
        will_rain = True
#mensagem chuva
if will_rain:
    #print("Leve seu guarda chuva")
    proxy_client = TwilioHttpClient()
    #responder twillio client
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="Vai chover hoje. Lembre-se de levar um ☔",
        from_="+12079528447",
        to="+5511964674101"
    )
    print(message.status)
