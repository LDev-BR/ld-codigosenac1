def caracteres():
    difer = set()
    palavra = input("Digite uma frase: ")
    difer.update(palavra)
    print("Números de caracteres diferentes: ")
    print(len(difer))
    print(difer)
caracteres()