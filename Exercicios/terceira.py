def notinhas():
    print('Bem-vindo')
    nota = float(input('Digite sua nota: '))
    if nota >= 7:
        print('Aprovado')
    elif nota < 4.99:
        print('Reprovado')
    else:
        print('Recuperação')
notinhas()