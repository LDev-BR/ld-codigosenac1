def clientes():
    #Educação em primeiro lugar sempre
    print('''           Bom dia''')
    #Lista de dados dos clientes
    dados = []
    #Loop de clientes
    for x in range(int(input('Digite o  número de clientes: '))):
        nome = input('Digite o nome: ')
        cpf = int(input('Digite o número do CPF: '))
        print('Cadastrado')
        infos = (nome, cpf)
        dados.append(infos)
    print(f'''Clientes cadastrados: {len(dados)}
''')
    #impressão dos clientes
    for n in dados:
        nome = n[0]
        cpf = n[1]
        print(f'''Nome: {nome} CPF: {cpf}
''')
clientes()
