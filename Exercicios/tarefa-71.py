import sqlite3
class conexaoBanco:
    def __init__(self, nome_banco = "livros.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.conexao.close()
class LivroDAO(conexaoBanco): # DAO - Data Acess Object
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            autor TEXT NOT NULL
            )
    ''')
    def inserir_livro(self, titulo, autor):
        self.cursor.execute('''
            INSERT INTO livros (titulo, autor) VALUES (?, ?)
    ''', (titulo, autor))
        self.conexao.commit()
        print(f"{titulo} de {autor} inserido com sucesso.")
    def listar_livro(self):
        self.cursor.execute('SELECT * FROM livros')
        livros = self.cursor.fetchall()
        print("\nLista de livros: ")
        for livro in livros:
            print(f"ID: {livro[0]} - Nome do Livro: {livro[1]} - Autor: {livro[2]}")
def menu():
    dao = LivroDAO()
    dao.criar_tabela()
    while True:
        print("\n1 - Inserir livro")
        print("2 - Listar livros")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            titulo = input("Digite o titulo do livro: ")
            autor = input("Digite o autor do livro: ")
            dao.inserir_livro(titulo, autor)
        elif opcao == "2":
            dao.listar_livro()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Opção inválida.")
menu()