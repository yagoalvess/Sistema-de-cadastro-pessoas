class Pessoa:
    def __init__(self,CPF,nome,dataNascimento) -> None:
        self.CPF = CPF
        self.nome = nome
        self.dataNascimento = dataNascimento


def main():
    p = Pessoa(13216,"Lucas","15-05-2000")
    print(p.dataNascimento)
main()