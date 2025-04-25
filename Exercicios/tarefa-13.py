def multiplos():
    numero_1 = int(input("Primeiro número: "))
    numero_2 = int(input("Segundo número: "))
    if numero_1 % numero_2 == 0:
        print("Os dois números são múltiplos um do outro")
    else:
        print("Os dois números não são múltiplos um do outro")

multiplos()