def bem_vindo():
    print('''
          Bem vindo amigo bonito.''')
def calculadora():
    operation = input('''
    Qual operação você deseja executar?:
    + Adição
    - Subtração
    * Multiplicação
    / Divisão
    ''')
    number_1 = int(input('Primeiro número: '))
    number_2 = int(input('Segundo número: '))
    #Soma
    if operation == '+':
        print('{} + {} ='.format(number_1, number_2))
        print(number_1 + number_2)
    #Subtração
    elif operation == '-':
        print('{} - {} ='.format(number_1, number_2))
        print(number_1 - number_2)
    #Multiplicação
    elif operation == '*':
        print('{} * {} ='.format(number_1, number_2))
        print(number_1 * number_2)
    #Divisão
    elif operation == '/':
        print('{} / {} ='.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print('Larga de ser burro, rode o programa novamente.')
    #Calcular denovo
    dnvo()
def dnvo():
    dnvo = input('''
Deseja calcular novamente?
S para SIM e N para NÂO.
''')
    if dnvo.upper() == 'S':
        calculadora()
    elif dnvo.upper() == 'N':
        print('Vlw.')
    else:
        dnvo()
bem_vindo()
calculadora()