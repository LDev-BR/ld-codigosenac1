def temperatura_atual():
    print('Bem vindo')
    temperatura = input('Quantos graus celsius está o clima de hoje?: ')
    if temperatura < '18':
        print('Está frio')
    elif temperatura > '25':
        print('Está quente')
    else:
        print('Tá dboa')
temperatura_atual()