from connect import inserir, mostrarTodos, deletarPessoa, atualizarPessoa
from model import Pessoa



#funções
def main():
    p = Pessoa(20000,"Amanda","30-05-2000")
    atualizarPessoa(49894,p)
    t = mostrarTodos()
    for c in t:
        print(c)
main()


