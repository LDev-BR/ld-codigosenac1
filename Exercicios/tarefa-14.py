def classificador():
    numeros = []
    positivos = 0
    negativos = 0
    zeros = 0
    for n in range(6):
        numero = int(input("Digite um número: "))
        numeros.append(numero)
        print("Número adicionado!")
    for n in numeros:
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
        else:
            zeros += 1
    print(f"{positivos} positivos, {negativos} negativos e {zeros} zeros")
classificador()