from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
''''DICA 1: Certifique-se de que você já fez login manualmente e verificou seu número de 
telefone com o Tinder, pois não podemos automatizar a verificação do número de telefone. Você só tem que fazer isso uma vez.
SUGESTÃO 2: Se você estiver obtendo uma NoSuchElementException, certifique-se de adicionar
algum atraso entre clicar nos botões para que o novo elemento tenha tempo suficiente para carregar.
DICA 3: Você pode achar mais fácil clicar com o botão direito do mouse no elemento
 e obter o XPath para usar com o Selenium.'''
GMAIL_EMAIL = ""
GMAIL_PASSWORD = ""

chrome_driver_path = ("C:\\Users\\pedro\\PycharmProjects\\chromedriver.exe")
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()

sleep(2)
fb_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

email.send_keys(GMAIL_EMAIL)
password.send_keys(GMAIL_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()