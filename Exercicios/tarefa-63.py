class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def saudacao(self):
        print(f"Olá, {self.nome}")
p = Pessoa("Lucas")
p.saudacao()

#Resposta: "Olá, Lucas"