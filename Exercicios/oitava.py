def notinhas():
    print('Bem-vindo')
    nota1 = int(input('Digite sua primeira nota: '))
    nota2 = int(input('Digite sua segunda nota: '))
    nota3 = int(input('Digite sua terceira nota: '))
    media = (nota1+nota2+nota3)/3
    print(f'Sua média é = {media}')
    if media > 7:
        print('Passou')
    elif media < 5:
        print('Você foi reprovado')
    else:
        print('Você ficou de recuperação')

notinhas()