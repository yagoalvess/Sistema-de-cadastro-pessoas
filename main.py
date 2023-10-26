from connect import *
from model import Pessoa



#funções
def main():
    p = Pessoa(20000,"Amanda","30-05-2000")
    t = mostrarTodos()
    for c in t:
        print(c)
    tt = mostrarTabelaTods()
    print(tt)
main()


