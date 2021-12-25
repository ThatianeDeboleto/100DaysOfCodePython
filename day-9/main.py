##Python Dictionaries

programa_dicionario = {
  "Bug": "Um erro em um programa que impede que o programa seja executado conforme o esperado.",
  "Function": "Um trecho de código que você pode chamar facilmente repetidamente.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
programa_dicionario["Loop"] = "A ação de fazer algo repetidamente."

#Create an empty dictionary.
vazio_dicionario = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programa_dicionario["Bug"] = "Uma maripousa em seu computador."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################

#Nesting
capitais = {
  "Franca": "Paris",
  "Germania": "Berlim",
  "Brasil": "Brasilia"
}

#Nesting a List in a Dictionary

viagem = {
  "Franca": ["Paris", "Lille", "Dijon"],
  "Germania": ["Berlim", "Hamburgo", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

viagem = {
  "France": {"cidades_visita": ["Paris", "Lille", "Dijon"], "total_visitas": 12},
  "Germany": {"cidades_visita": ["Berlin", "Hamburg", "Stuttgart"], "total_visitas": 5},
}

#Nesting Dictionaries in Lists

viagem = [
{
  "pais": "France",
  "cidade_visita": ["Paris", "Lille", "Dijon"],
  "total_visitas": 12,
},
{
  "pais": "Germany",
  "cidade_visita": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visitas": 5,
},
]
