from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
#introducao de dados de investigação beautifulsoup + selenium
#day47 #http://myhttpheader.com/ dados para preenchimento
header = {
    "User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64481581640625%2C%22east%22%3A-122.22184218359375%2C%22south%22%3A37.64220115428586%2C%22north%22%3A37.908142595089735%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D")
data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".list-card-top a")
#https://docs.google.com/spreadsheets/d/1jkmjJSKojSFWbQPOB2i66aC6754eG7HXg7S08T4Zgz8/edit?resourcekey#gid=2115540022
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

all_price_elements = soup.select(".list-card-details li")
all_prices = [price.get_text().split("+")[0] for price in all_price_elements if "$" in price.text]


chrome_driver_path = "C:\\Users\\pedro\\PycharmProjects\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdoGsfsGBwEgyD8g-w3LavDP_cUCvpDn_CJNtYBWNM_D8SQIA/viewform?usp=sf_link")
    
    time.sleep(2)
    # preencher formulario
    # inspecionar - clicar seta - selecionar - copiar XPath
    endereco = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    preco = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    clicar_botao = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    endereco.send_keys(all_addresses[n])
    preco.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    clicar_botao.click()



''''from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
element = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.ID, "id-of-new-element"))
)
finally:
driver.quit()'''