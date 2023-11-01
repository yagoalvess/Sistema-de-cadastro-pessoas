from flask import Flask, render_template, redirect
from connect import *
from model import Pessoa
from flask.globals import request


app = Flask(__name__)


# Paginas
@app.route("/")
def homepage():
    result = mostrarTodos()
    return render_template("homepage.html",result = result)


# função
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    cpf = request.form["cpf"]
    dataNascimento = request.form["dataNascimento"]
    pessoa = Pessoa(cpf,nome,dataNascimento)
    inserir(pessoa)
    return redirect("/")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/cadastro_usuario")
def usuarios():
    return render_template("cadastro_usuario.html",)


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)







