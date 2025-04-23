def classificar_numeros():
    positivos = 0
    negativos = 0
    zeros = 0

    for i in range (6):
        numero = float(input('Digite o número: '))
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            zeros +=1

    print(f'Positivos: {positivos}')
    print(f'Negativos: {negativos}')
    print(f'Zeros: {zeros}')

classificar_numeros()