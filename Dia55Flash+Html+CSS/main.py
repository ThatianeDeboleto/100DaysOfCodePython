from flask import Flask

app = Flask(__name__)

#Decoradores para adicionar uma tag ao redor do texto na página da web.
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def site():
    #Renderizando Elementos HTML
    return '<h1 style="text-align: center">Olá, sou um Bot e me chamo Ômega. Estou em construção!</h1>' \
           '<p style="text-align: center">Estou sendo desenvolvido por uma humana, que esta ' \
           'ingressando agora na área de tecnologia.</p>' \
           '<img src="https://i.pinimg.com/originals/b9/f8/51/b9f851908b8b24e0f2a1812e83a9da52.gif" width=200 >'


#Rotas diferentes usando o decorador app.route
#http://127.0.0.1:5000/bye
#enfase em estrutura na palavra escurecer, sublinhar....
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    #b deixa em negrito
    return "<b>Espero te ver em breve!<b>"
#caso deseje adicionar um numero se deve acrescenta /<int:number> http://127.0.0.1:5000/username/NOME/12
#basta adicionar o nome a barra de pesquisa
#Criação de caminhos de variáveis e conversão do caminho para um tipo de dados especificado
@app.route("/username/<name>")
def greet(name):
    return f"Olá {name}!"


if __name__ == "__main__":
    #Execute o aplicativo no modo de depuração para recarregar automaticamente
    app.run(debug=True)



#Agora é hora de concluir o projeto final do dia, o jogo inferior mais alto que criamos no Dia 14,
# mas agora com um site real.