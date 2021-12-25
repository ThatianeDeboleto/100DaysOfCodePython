from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
''''classes e objetos em Python extensivamente nos dias 16-20, 
este pode ser um bom momento para revisar essas lições se você não consegue se lembrar de como fazer as etapas acima.'''
PROMISED_DOWN = 60
PROMISED_UP = 24
#caminho para o chrome instalado na maquina - caso seja outro servidor leia a documentacao
# utilizando \ no windowns para não dar erro coloque \\ ou r"caminho"
CHROME_DRIVE_PATH = ""
TWITTER_EMAIL = ''
TWITTER_PASSWORD = ''


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0
#acesso a pagina da velocidade para informar a velocidade ao qual foi solicitada
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        accept_button.click()
        time.sleep(3)

        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        time.sleep(3)
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input').text
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input').text
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').text
        tweet = f"Ei, provedor de Internet, por que minha velocidade de Internet{self.down}baixar/{self.up}quando eu pagar por {PROMISED_DOWN}baixar/{PROMISED_UP}subir?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()

bot = InternetSpeedTwitterBot(CHROME_DRIVE_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()