# ####Introdução ao Web Scraping#####
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
#codigo da pagina - inspect
#print(response.text)
yc_web_page = response.text
#analisar a parte ao qual se deseja
soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
# <title>Hacker News</title>
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)



largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

# print(article_texts[largest_index])
# print(article_links[largest_index])


# #BeautifulSoup: é um modulo que ajuda os programadores a dar sentido aos sítios web
# from bs4 import BeautifulSoup
#
# #chamar html
# with open("website.html") as file:
#     contents = file.read()
#
# #É assim que você faz para criar usar a funcao soup
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
# # print(soup.title.string)
#
# # Prettify will add indentation to the soup.
# # print(soup)
# # print(soup.prettify())
#
# # Você pode acessar a primeira tag de qualquer tipo usando .p ou .a ou .h1 etc.
# # print(soup.p)
#
# # Você pode criar uma lista de todas as ocorrências de tag com find_all ()
# #mostrar links html e nomes html
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # imprimir os textos que ancora os links
# # for tag in all_anchor_tags:
#     #getText() gets the text in the tag.
#     # print(tag.getText())
#     # get() can get the value of any tag attribute.
#     #somente os LINKS
#     # print(tag.get("href"))
#
# # find () funciona como find_all (), mas apenas obtém a primeira ocorrência.
# # Você também pode encontrar por id.
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# #Você também pode encontrar por class_ name.
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
# # print(section_heading.name)
# # print(section_heading.get("class"))
#
# #Você também pode encontrar usando um Seletor CSS:
# print(soup.select_one(selector=".company a"))
# print(soup.select("a"))



