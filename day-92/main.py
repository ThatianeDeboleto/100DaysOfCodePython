from twitter_bot import TwitterBot

CHROME_DRIVER_PATH = "***************"


def take_input(message):
    s = input(message)
    no_of_images = int(input("Quantas imagens você deseja baixar ?: "))
    return (s, no_of_images)


print("📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷")
print("Bem vindo ao Download de imagens")
print("📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷📷")
print("1) Por nome de usuário")
print("2) Por Hashtag")
print("3) Por pesquisa")
choice = int(input("Digite sua escolha: "))

bot = TwitterBot(CHROME_DRIVER_PATH)

if choice == 1:
    username, no_of_images = take_input("Insira nome de usuário: ")
    bot.find_by_username(username, no_of_images=no_of_images)
elif choice == 2:
    hashtag, no_of_images = take_input("Insira a hashtag: ")
    bot.find_by_hashtag(hashtag, no_of_images=no_of_images)
elif choice == 3:
    query, no_of_images = take_input("Insira o valor da pesquisa: ")
    bot.find_by_search(query, no_of_images=no_of_images)
else:
    print("Escolha inválida!")

bot.close()

