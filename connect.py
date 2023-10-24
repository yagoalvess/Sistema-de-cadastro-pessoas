from tinydb import TinyDB,Query
from model import Pessoa


db = TinyDB("Pessoas.json")
usuario = Query()




#inserir no banco json os dados da pessoa
def inserir(model: Pessoa):
    db.insert({"CPF":model.CPF,"Nome":model.nome, "DataNascimento":model.dataNascimento})
    print("Pessoa registrada com sucesso")


#mostrar o dados no banco na tela 
def mostrarTodos():
    todos = db.all()
    return todos


# deletar a pessoa no banco de dados
def deletarPessoa(cpf: int):
    if db.search(usuario.CPF==cpf):
        db.remove(usuario.CPF==cpf)
        print("Usuario deletado com sucesso")
    else:
        print("Usuario não encontrado")
