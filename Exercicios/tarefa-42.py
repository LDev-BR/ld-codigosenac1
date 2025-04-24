def pares():
    pares = []
    impares = []
    while True:
        numero = int(input("Seu número: "))
        if numero == 0:
            break
        if numero%2 == 0:
            pares.append(numero)
        elif numero%2 != 0:
            impares.append(numero)
    print(pares)
pares()
