from tinydb import TinyDB
from model import Pessoa


db = TinyDB("Pessoas.json")

#inserir no banco json os dados da pessoa
def inserir(model: Pessoa):
    db.insert({"CPF":model.CPF,"Nome":model.nome, "DataNascimento":model.dataNascimento})


#mostrar o dados no banco na tela 
def mostrarTodos():
    todos = db.all()
    return todos

