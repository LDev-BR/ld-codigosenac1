import sqlite3
class conexaoBanco:
    def __init__(self, nome_banco = "gpus.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.conexao.close()
class gpuDAO(conexaoBanco): # DAO - Data Acess Object
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS gpus(
                            nome TEXT NOT NULL,
                            preco FLOAT NOT NULL
            )
    ''')
    def inserir_gpu(self, nome, preco):
        self.cursor.execute('''
            INSERT INTO gpus (nome, preco) VALUES (?, ?)
    ''', (nome, preco))
        self.conexao.commit()
        print(f"{nome} de R$ {preco} inserido com sucesso.")
    def listar_gpu(self):
        self.cursor.execute('SELECT * FROM gpus')
        gpus = self.cursor.fetchall()
        print("\nLista de gpus: ")
        for gpu in gpus:
            print(f"Nome do gpu: {gpu[0]} - preco: R$ {gpu[1]}")
    def atualizar(self, nome, novo_preco):
        self.cursor.execute('UPDATE gpus SET preco = ? WHERE nome = ?', (novo_preco, nome))
        self.conexao.commit()
        print(f"preco de {nome} atualizada para {novo_preco}")
def menu():
    dao = gpuDAO()
    dao.criar_tabela()
    while True:
        print("\n1 - Inserir gpu")
        print("2 - Listar gpus")
        print("3 - Atualizar")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do gpu: ")
            preco = input("Digite o preco do gpu: ")
            dao.inserir_gpu(nome, preco)
        elif opcao == "2":
            dao.listar_gpu()
        elif opcao == "3":
            novo_preco = float(input("Digite o novo preço: "))
            nome = input("Digite o nome: ")
            dao.atualizar(nome, novo_preco)
        elif opcao == "4":
            dao.fechar()
            break
        else:
            print("Opção inválida.")
menu()