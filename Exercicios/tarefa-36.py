import statistics
def med():
    numeros = []
    for n in range(int(input("Digite quantos números você deseja incluir: "))):
        numero = int(input("Digite o número: "))
        numeros.append(numero)
    print('A média é: ', (statistics.mean(numeros)))
    print('A mediana é: ', statistics.median(numeros))
    print('A moda é: ', statistics.mode(numeros))

med()