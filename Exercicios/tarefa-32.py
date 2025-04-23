import random
print('Bom dia')
def dadosrpg():
    numero = random.randint(1, int(input('''Digite o número do D do dado: ''')))
    print('O resultado foi: ', numero)
    nov = (str(input("Deseja rolar o dado novamente? (s) para SIM e (n) para NÃO: ")))
    if nov == "s":
        dadosrpg()
    else:
        print("Valeu")
dadosrpg()