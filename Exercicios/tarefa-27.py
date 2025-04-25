def senha_loop():
    senha = input("Digite sua senha: ")
    while True:
        confirm = input("Confirme sua senha: ")
        if confirm == senha:
            print("Senha criada com sucesso!")
            break

senha_loop()