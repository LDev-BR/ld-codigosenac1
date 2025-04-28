def bem_vindo():
    print('Bem vindo ao programa')
def combustivel():
    gasolina = 5.39
    alcool = 4.39
    diesel = 5.99
    total = float(input('Quantos litros de gasolina você deseja abastecer?: '))
    operation = str(input('''
    Qual o combustível desejado?:
    G Gasolina
    A Álcool
    D Diesel
    ''')).upper()
    if operation == 'G':
        print(f'O total foi: {total * gasolina}')
    elif operation == 'A':
        print(f'O total foi: {total * alcool}')
    elif operation == 'D':
        print(f'O total foi: {total * diesel}')
    else:
        print('Inválido')
    dnvo()

def dnvo():
    dnvo = input('''
Deseja abastecer novamente?
S para SIM e N para NÂO.
''')
    if dnvo.upper() == 'S':
        combustivel()
    elif dnvo.upper() == 'N':
        print('Vlw.')
    else:
        dnvo()
bem_vindo()
combustivel()