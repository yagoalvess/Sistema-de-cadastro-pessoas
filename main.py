from connect import inserir, mostrarTodos, deletarPessoa
from model import Pessoa



#funções
def main():
    p = Pessoa(5000,"Amanda","30-05-2000")
    inserir(p)
    t = mostrarTodos()
    for c in t:
        print(c)
main()


