def imc():
    print('Calculadora de IMC')
    peso = float(input('Qual seu peso em Kilogramas?: '))
    altura = float(input('Qual sua altura em Metros?: '))
    imc_total = peso/(altura ** 2)
    print(f'{imc_total}')
    if imc_total > 30:
        print('Você está obeso')
    elif imc_total < 18.5:
        print('Você se encontra na abaixo do peso')
    elif imc_total >= 18.5 < 25:
        print('Você se encontra na faixa normal de peso')
    elif imc_total >= 25 < 30:
        print('Você está na faixa do sobrepeso')
    else:
        print('Inválido')
    dnvo()

def dnvo():
    dnvo = input('''
Deseja calcular novamente?
S para SIM e N para NÂO.
''')
    if dnvo.upper() == 'S':
        imc()
    elif dnvo.upper() == 'N':
        print('Obrigado por usar nossa calculadora')
    else:
        dnvo()

imc()