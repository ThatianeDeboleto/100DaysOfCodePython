from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

header = {
    "User-Agent":  "",
    "Accept-Language": ""
}
response = requests.get(
""    headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".list-card-top a")

all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    # Obtenha os preços. Listagens únicas e múltiplas têm diferentes tags e estruturas de classe
    try:
        # Preço com apenas uma listagem
        preco = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        # Preço com várias listagens
        preco = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(preco)


# Criar planilha usando o Formulário Google - ok
chrome_driver_path = ""
driver = webdriver.Chrome('./chromedriver')

for n in range(len(all_links)):
    driver.get("")

    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("26/11/2021")
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
        "565 Webster St #C,  San Francisco, CA 94117")
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
        "https://www.zillow.com/homedetails/565-Webster-St-C-San-Francisco-CA-94117/2067446546_zpid/")
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

    # endereco.send_keys(all_addresses[n])
    # preco.send_keys(all_prices[n])
    # link.send_keys(all_links[n])
    # clicar_botao.click()