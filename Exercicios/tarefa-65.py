class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def mostrar_idade(self):
        print(f"O aluno {self.nome} possui {self.idade}")

aluno1 = Aluno("Luis", 21)
aluno1.mostrar_idade()