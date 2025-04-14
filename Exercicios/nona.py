def caixa():
    print('Saque seu dinheiro, disponível: R$ 100,00')
    operacao = int(input('Digite o quanto você deseja sacar '))
    if operacao == "100":
        print('1 nota de R$: 100 sendo sacada')
    elif operacao == '50':
        print('1 nota de R$: 50 sendo sacada')
    elif operacao == "20":
        print('1 nota de R$: 20 sendo sacada')
    elif operacao == '10':
        print('1 nota de 10 sendo sacada')
    else:
        print('Burro')

caixa()