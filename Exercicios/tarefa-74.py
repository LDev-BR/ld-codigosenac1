import sqlite3
class conexaoBanco:
    def __init__(self, nome_banco = "clientes.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.conexao.close()
class clienteDAO(conexaoBanco): # DAO - Data Acess Object
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL
            )
    ''')
    def inserir_cliente(self, nome, email):
        self.cursor.execute('''
            INSERT INTO clientes (nome, email) VALUES (?, ?)
    ''', (nome, email))
        self.conexao.commit()
        print(f"{nome} de {email} inserido com sucesso.")
    def listar_cliente(self):
        self.cursor.execute('SELECT * FROM clientes')
        clientes = self.cursor.fetchall()
        print("\nLista de clientes: ")
        for cliente in clientes:
            print(f"ID: {cliente[0]} - Nome do cliente: {cliente[1]} - email: {cliente[2]}")
def menu():
    dao = clienteDAO()
    dao.criar_tabela()
    while True:
        print("\n1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            dao.inserir_cliente(nome, email)
        elif opcao == "2":
            dao.listar_cliente()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Opção inválida.")
menu()