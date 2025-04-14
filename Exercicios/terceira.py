def notinhas():
    print('Bem-vindo')
    nota = input('Digite sua nota: ')
    if nota > '7':
        print('Aprovado')
    elif nota < '5':
        print('Reprovado')
    else:
        print('Recuperação')
notinhas()