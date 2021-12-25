import requests
from datetime import datetime
import os
#genero, peso, altura, idade
GENDER = ""
WEIGHT_KG = 47
HEIGHT_CM = 157
AGE = 26
#API DO SITE https://developer.nutritionix.com/admin/access_details
APP_ID = ""
API_KEY = ""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = ""
#Quais exercicios fez - lingua ingles - site nao traduz Ex Res correr 8k e pedalar e 14 minutos // run 8k and cycle and 14 minutes
exercise_text = input("Tell me which exercises you did: ")
#cabeçalhos busca id do inicio
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
#busca das especificacoes do site e adcionada ao codigo
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
#uso json utilizado para estruturar dados em formato de texto e permitir a troca de dados entre aplicações
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
#Dia e tempo FORMATO D/M/A e tempo
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
#exercicios da pagina nutri e especificacoes da tabela google para site seets
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "data": today_date,
            "tempo": now_time,
            "exercicio": exercise["name"].title(),
            "duracao": exercise["duration_min"],
            "calorias": exercise["nf_calories"]
        }
    }

    #Autenticacao
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


    #Basica Autenticacao
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            "Thatiane Rosa Gomes Nimtzz",
            "Deussep5",
        )
    )

    #Símbolo ATIVACAO // token de acesso para acessar os dados de um usuário pela API
    bearer_headers = {
    "Authorization": f"Bearer {'TOKEN'}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
