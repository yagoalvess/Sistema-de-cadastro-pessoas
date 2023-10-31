from flask import Flask, render_template
from connect import *
from model import Pessoa

app = Flask(__name__)


# Paginas
@app.route("/")
def homepage():
    result = mostrarTodos()
    return render_template("homepage.html",result = result)


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/cadastro_usuario")
def usuarios():
    return render_template("cadastro_usuario.html",)


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)



