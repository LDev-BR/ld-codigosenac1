def classificador():
    letras = []
    a = 0
    for n in range(5):
        letra = input("Digite uma letra: ")
        letras.append(letra)
    for n in letras:
        if n.startswith("A"):
            a += 1
        elif n.startswith("a"):
            a += 1
    print("Palavras que começam com (a): ",a)
classificador()