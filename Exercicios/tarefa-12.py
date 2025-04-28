import statistics
def med():
    numeros = []
    for n in range(5):
        numero = int(input("Digite o número: "))
        numeros.append(numero)
    media = statistics.mean(numeros)
    print('A média é: ', media)
    if media >= 7:
        print("Passou")
    elif media < 5:
        print("Reprovado")
    else:
        print("Recuperação")
med()