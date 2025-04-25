def multiplos():
    numeros = []
    pares = 0
    impares = 0
    for n in range(7):
        numero = int(input("Digite seu número: "))
        numeros.append(numero)
        print("Número adcionado")
    for n in numeros:
        if n % 2 == 0:
            pares += 1
        if n % 2 != 0:
            impares += 1
    print("-Número de pares: ",pares,"-Número de impares: ",impares)
multiplos()