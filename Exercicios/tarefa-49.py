def paises_sul():
    paises = {
        "Brasil",
        "Argentina",
        "Paraguai"
    }
    for n in range(3):
        nome = input("Digite um nome de país: ")
        if nome in paises:
            print("Pertence ao conjunto")
        else:
            print("Não pertence ao conjunto")
paises_sul()