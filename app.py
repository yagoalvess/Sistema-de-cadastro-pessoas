from model import Pessoa
from connect import inserir
from flask import Flask, render_template

app = Flask(__name__)


# Paginas
@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/cadastro_usuario")
def usuarios():
    return render_template("cadastro_usuario.html",)


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)



#função para salvar dados no banco de dados
def main():
    p = Pessoa(13216,"Lucas","15-05-2000")
    inserir(p)
main()