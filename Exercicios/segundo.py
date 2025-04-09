def desconto():
    valor = float(input('Digite o valor do produto e receba seu desconto: '))
    if valor >= 100:
        reducao = valor*0.1
        print(f'Seu desconto é de: {reducao}')
    elif valor <= 99:
        print('Sem desconto para você')
    else:
        print('Burro')

desconto()