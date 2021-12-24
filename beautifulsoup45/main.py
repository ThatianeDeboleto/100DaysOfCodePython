import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


'''
FAQ: O site da Empire mudou!

Quando esta lição foi criada, usei este URL para o projeto:
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

No entanto, Empire desde então mudou seu site. Você pode ver isso ao inspecionar os elementos do título do filme.
Você verá que o h3 com a classe "title" não está mais lá.
Para usar exatamente o mesmo código da solução, podemos usar uma versão em cache do site da Wayback Machine do Internet Archive.
'''