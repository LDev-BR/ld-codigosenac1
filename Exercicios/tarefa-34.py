def cronometro():
    segundo =  int(input("Digite quantos segundos você deseja: "))
    for s in range(segundo):
        if segundo > 0:
            segundo - 1
            print(segundo)
        else:
            print("Fim.")
cronometro()