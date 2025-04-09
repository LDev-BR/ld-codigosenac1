def festa():
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        print('Bem-vindo a party')
    elif idade <= 17:
        print('Vaza')
    else:
        print('Burro')

festa()