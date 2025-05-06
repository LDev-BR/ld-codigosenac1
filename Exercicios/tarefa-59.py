#Instanciar uma classe é dar um valor ao objeto por ex:
class Npc:
    def __init__(self, nome, hp, raca, classe):
        self.nome = nome
        self.hp = hp
        self.raca = raca
        self.classe = classe
    def printar_npc(self):
        print(f"Nome do NPC: {self.nome} HP: {self.hp} Raça: {self.raca} Classe: {self.classe}")
npc1 = Npc("Luis", 100, "Meio-Elfo", "Paladino") #Isto é instanciar um objeto
npc1.printar_npc()