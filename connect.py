from tinydb import TinyDB
from model import Pessoa


db = TinyDB("Pessoas.json")

def inserir(model: Pessoa):
    db.insert({"CPF":model.CPF,"Nome":model.nome, "DataNascimento":model.dataNascimento})