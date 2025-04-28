def tabuada():
    numero = int(input("Digite um número para ver sua tabuada de 10: "))
    for n in range(1, 11):
        print(f"{numero} x {n} = {numero * n}")
tabuada()