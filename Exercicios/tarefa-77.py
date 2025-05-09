import sqlite3
class conexaoBanco:
    def __init__(self, nome_banco = "lanches.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.conexao.close()
class lancheDAO(conexaoBanco): # DAO - Data Acess Object
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS lanches(
                            nome TEXT NOT NULL,
                            preco FLOAT NOT NULL
            )
    ''')
    def inserir_lanche(self, nome, preco):
        self.cursor.execute('''
            INSERT INTO lanches (nome, preco) VALUES (?, ?)
    ''', (nome, preco))
        self.conexao.commit()
        print(f"{nome} de R$ {preco} inserido com sucesso.")
    def listar_lanche(self):
        self.cursor.execute('SELECT * FROM lanches')
        lanches = self.cursor.fetchall()
        print("\nLista de lanches: ")
        for lanche in lanches:
            print(f"Nome do lanche: {lanche[0]} - preco: R$ {lanche[1]}")
def menu():
    dao = lancheDAO()
    dao.criar_tabela()
    while True:
        print("\n1 - Inserir lanche")
        print("2 - Listar lanches")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do lanche: ")
            preco = input("Digite o preco do lanche: ")
            dao.inserir_lanche(nome, preco)
        elif opcao == "2":
            dao.listar_lanche()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Opção inválida.")
menu()