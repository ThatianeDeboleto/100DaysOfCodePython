from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Para qual ano você quer viajar? Digite a data neste formato AAAA-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="",
        client_id="",
        client_secret="",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Procurando músicas no Spotify por título
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} não existe no Spotify. Pulado.")

#Criação de uma nova lista de reprodução privada no Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adicionando músicas encontradas na nova lista de reprodução
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
