def produtos_loja():
    produtos = set()
    media = 0
    for n in range(3):
        product = input("Digite o nome do produto: ")
        preco = float(input("Digite um número: "))
        media += preco
        td = product, preco
        produtos.add(td)
    print("Produtos disponíveis: \n")
    for produto, preco in produtos:
        print(f"Nome do produto: ",produto)
        print(f"Preço do produto: {preco}\n")
    print(f"A média dos preços é: ", media/3)
produtos_loja()