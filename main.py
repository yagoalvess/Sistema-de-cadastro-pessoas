from connect import inserir, mostrarTodos
from model import Pessoa


#função para salvar dados no banco de dados
def main():
    p = Pessoa(13216,"Lucas","15-05-2000")
    inserir(p)
main()


#função para monstrar os dados salvados no banco
def main():
    p = Pessoa(2910312093821803912,"Jorge","30-05-2000")
    #inserir(p)
    t = mostrarTodos()
    for c in t:
        print(c)
main()