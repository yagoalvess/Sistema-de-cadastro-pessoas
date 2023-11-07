from flask import Flask, render_template, redirect
from connect import *
from model import Pessoa
from flask.globals import request
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os


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


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)



# configuração para aws
def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\n"
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()


