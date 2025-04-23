#Função inicial
def conversor():
    print('''           Bem vindo!''')
    escolha = input('''
    Escolha sua conversão para ser feita?:
    (D) - Dólar para real
    (R) - Real para dólar
    (S) - Sair
    ''')
    if escolha == 'D':
        conversor_real()
    if escolha == 'R':
        conversor_dolar()
    if escolha == 'S':
        print('Passar bem')
#Conversor de real para dólar
def conversor_real():
    dolar = 5.90
    real = float(input('Digite o valor em dólar: '))
    valor = (real*dolar)
    if valor > 0:
        print(f'O seu valor é: R$: {valor}')
    else:
        print('Apenas valores maiores que 0 são válidos')
    denovo()
#Conversor de dólar para real
def conversor_dolar():
    real = 0.17
    dolar = float(input('Digite o valor em real: '))
    valor = (dolar*real)
    if valor > 0:
        print(f'O seu valor é: $: {valor}')
    else:
        print('Apenas valores maiores que 0 são válidos')
    denovo()
#Recomeçar
def denovo():
    print('Deseja começar denovo?')
    escolha = input('(S) para SIM e (N) para NÃO: ')
    if escolha == 'S':
        conversor()
    if escolha == 'N':
        print('Passar bem')
conversor()