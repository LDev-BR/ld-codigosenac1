import random
def aleatorio():
    choice = random.randint(1, 10)
    for n in range(3):
        escolha = int(input("Tente acertar o número da sorte: "))
        if escolha == choice:
            print("Certa resposta")
            return
        elif escolha > choice:
            print("O número da sorte é menor")
        elif escolha < choice:
            print("O número da sorte é maior")
        else:
            print("Escolha um caractere válido.")
    print("O número secreto era: ", choice)
aleatorio()