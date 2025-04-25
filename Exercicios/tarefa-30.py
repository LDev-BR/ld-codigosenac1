def contador():
    for i in range(3):
        palavra = input("Digite a palavra: ")
        vogais = 0
        consoantes = 0
        espacos = 0
        for letra in palavra.lower():
            if letra in "aeiou":
                vogais += 1
            elif letra == " ":
                espacos += 1
            elif letra.isalpha():
                consoantes += 1
        print(f"O resultado da {palavra} é: ")
        print("Vogais: ", vogais)
        print("Espaços: ", espacos)
        print("Consoantes: ", consoantes)
contador()