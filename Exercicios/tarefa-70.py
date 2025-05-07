#Metódos são todas as funções dentro de uma classe e como elas afetam o objeto e instâncias são a realização das classes, exemplo:

class Npc:
    def __init__(self, nome, raca, classe, lvl, hp): #Metódo gerador que da valores a serem adcionados pelas instâncias no objeto
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.lvl = lvl
        self.hp = hp
    def printar_npc(self): #Metódo PrintarNPC
        print(f"{self.nome}/{self.raca} - HP: {self.hp}")
        print(f"{self.classe} - LVL = {self.lvl}")
npc1 = Npc("Luis", "Meio-Elfo", "Paladino - Juramento da Vingança", 20, 200)#Instância npc que possui seus próprios valores
npc1.printar_npc() #Chama o metódo Printar NPC