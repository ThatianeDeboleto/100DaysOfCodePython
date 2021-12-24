import requests
import lxml
from bs4 import BeautifulSoup
#http://myhttpheader.com/
url = "https://www.amazon.com.br/Kindle-10a-gera%C3%A7%C3%A3o-ilumina%C3%A7%C3%A3o-embutida/dp/B07FQK1TS9/ref=sr_1_4?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=kindle&qid=1637689606&sr=8-4&ufe=app_do%3Aamzn1.fos.95de73c3-5dda-43a7-bd1f-63af03b14751"
header = {
    "User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())


title = soup.find(id = "productTitle").get_text()

print(title)

# price = soup.find(id="priceblock_ourprice").get_text()
# price_without_currency = price.split("$")[1]
# price_as_float = float(price_without_currency)
# print(price_as_float)