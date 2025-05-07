class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    def desconto(self):
        desconto10 = self.valor - (self.valor * 0.1)
        print(desconto10)

produto1 = Produto("Salada", 100)
produto1.desconto()