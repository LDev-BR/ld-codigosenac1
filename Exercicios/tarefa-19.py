def vogais():
    palavra = input("Digite uma palavra: ").lower()
    vogais = 0
    for n in palavra:
        if n in "aeiou":
            vogais += 1
    print(vogais)
vogais()