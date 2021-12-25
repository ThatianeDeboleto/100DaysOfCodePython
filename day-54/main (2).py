#instalação Flask- Introducao

from flask import Flask
#uma classe para aplicacao no Flask
app = Flask(__name__)
#@ decoretor uma funcao para acrescentar mais uma funcionalidade adicional a uma funcao ja existente.
@app.route('/')
def site():
    return "Ola, sou um 🤖 e me chamo Sabedoria!"

@app.route("/bye")
def site_bye():
    return "Estou em construção, espero te ver em breve aqui!"

#execucao do codigo -controle padrao
if __name__ == "__main__":
    app.run(debug=True)


#decoreitor windowns para funcao
# @app.route("/")
# def index():
#     return "Index"
#
# if __name__ == '__main__':
#     app.run()