def desconto():
    valor_1 = float(input('Digite o valor do primeiro produto: '))
    valor_2 = float(input('Digite o valor do segundo produto: '))
    valor_3 = float(input('Digite o valor do terceiro produto: '))
    valor_4 = float(input('Digite o valor do quarto produto: '))
    valor_total = (valor_1+valor_2+valor_3 + valor_4)
    if valor_total > 200:
        reducao = valor_total - (valor_total*0.1)
        print(f'Seu valor com 10% de desconto é: R$: {reducao}')
    elif valor_total > 100:
        reducao_2 = valor_total - (valor_total*0.05)
        print(f'Seu valor com 5% de desconto é: R$: {reducao_2}')
    else:
        print('Sem desconto pra você')

desconto()