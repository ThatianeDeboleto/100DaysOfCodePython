import requests
import lxml
from bs4 import BeautifulSoup
#http://myhttpheader.com/
url = ""
header = {
    "User-Agent":  "",
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