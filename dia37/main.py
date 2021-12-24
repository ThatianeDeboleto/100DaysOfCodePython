import requests
from datetime import datetime

#projeto utilizando cabeçalho - POST PUT DELETE
USERNAME = "thati"
TOKEN = "1hjkkklopahsgdvgfiilm"
GRAPH_ID = "graph2"

pixela_endpoint = "https://pixe.la/v1/users"
#https://docs.pixe.la/entry/post-user
user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## POST CONFIRMAR CRIOU O UTILIZADOR
# message:"Success. Let's visit https://pixe.la/@thati , it is your profile page!","isSuccess":true
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#cores shibafu(verde), momiji(vermelho),sora(azul),ichou(amarelo),ajisai(roxo),kuro(preto).
graph_config = {
    "id": GRAPH_ID,
    "name": "graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}
#teste
# response = requests.post(url=graph_endpoint, json=graph_config)
# print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))
#armazenar valor no grafico
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many kilometers did you walk today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

#HTML
#requests.get(colocar parametros dentro dos parenteses)



# https://pixe.la/v1/users/thati/graphs/graph2.html