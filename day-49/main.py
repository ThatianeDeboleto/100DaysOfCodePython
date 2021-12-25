from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
#dados para abrir o linkedin na pagina diretamente na conta
ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""
PHONE = ""

chrome_driver_path = ("")
driver = webdriver.Chrome(chrome_driver_path)
driver.get("")
#botao click para chegar a vaga
time.sleep(2)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()
#dados da conta ativada para acesso a vaga = preenchimento vaga
time.sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
#função para adicionar um atraso de tempo ao seu código. Esta função é útil se você deseja pausar seu código
# entre chamadas de API,
# por exemplo. Ou melhore a experiência do usuário adicionando pausas entre palavras ou gráficos.
time.sleep(5)
#seletor de vagas
all_listings = driver.find_elements_by_css_selector(
    ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(
            ".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)
#dados vaga assinar automaticamente
        '''Carregue o seu currículo indo para Mim -> Configurações e privacidade -> 
        Preferências de busca de emprego -> Configurações do formulário de emprego'''
        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name(
                "artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_elements_by_class_name(
                "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name(
            "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

#projeto possui falhas devido ao nivel de seguranca do LinkedIn para os usuários
''''Ocasionalmente, o LinkedIn mostrará um Captcha quando você fizer login, que deverá ser preenchido manualmente.'''
'''O objetivo do projeto de hoje é aprender a usar o Selenium para automatizar a candidatura a empregos.
Assim, ao final de hoje, você deve ter um programa que pode usar a função "Easy Apply" do LinkedIn 
para enviar candidaturas a todas as vagas que atendam aos seus critérios (em vez de apenas uma única lista).'''''