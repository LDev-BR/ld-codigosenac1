class Circulo:
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return 3.14 * (self.raio ** 2)
c = Circulo(2)
print(c.area())

#Resposta 12.56