def primo():
    primo = 1
    numero = int(input("Digite um número: "))
    for n in range(2, numero):
        if numero % n == 0:
            primo = 0
    if primo == 1:
        print("O número é primo.")
    else:
        print("O número não é primo.")
primo()