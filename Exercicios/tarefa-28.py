def tabuada():
    numero = int(input("Digite um número para ver sua tabuada de 10: "))
    for n in range(1, 11):
        print(f"{numero} x {n} = {numero * n}")
    dnvo()
def dnvo():
    dnvo = input('''
Deseja calcular novamente?
S para SIM e N para NÂO.
''')
    if dnvo.upper() == 'S':
        tabuada()
    elif dnvo.upper() == 'N':
        print('Vlw.')
    else:
        dnvo()
tabuada()