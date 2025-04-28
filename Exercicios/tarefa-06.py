def senha_verificacao():
    senha = input('Digite sua senha: ')
    if senha == 'senac123':
        print('Entrou')
    elif senha != 'senac123':
        print('Senha incorreta')
        senha_verificacao()
senha_verificacao()