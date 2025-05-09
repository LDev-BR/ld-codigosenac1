import sqlite3
class conexaoBanco:
    def __init__(self, nome_banco = "livros.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.conexao.close()
class livroDAO(conexaoBanco): # DAO - Data Acess Object
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros(
                            nome TEXT NOT NULL,
                            autor TEXT NOT NULL
            )
    ''')
    def inserir_livro(self, nome, autor):
        self.cursor.execute('''
            INSERT INTO livros (nome, autor) VALUES (?, ?)
    ''', (nome, autor))
        self.conexao.commit()
        print(f"{nome} de {autor} inserido com sucesso.")
    def listar_livro(self):
        self.cursor.execute('SELECT * FROM livros')
        livros = self.cursor.fetchall()
        print("\nLista de livros: ")
        for livro in livros:
            print(f"Nome do livro: {livro[0]} - autor: {livro[1]}")
    def atualizar(self, nome, novo_autor):
        self.cursor.execute('UPDATE livros SET autor = ? WHERE nome = ?', (novo_autor, nome))
        self.conexao.commit()
        print(f"autor de {nome} atualizada para {novo_autor}")
    def deletar(self, nome_remover):
        self.cursor.execute('DELETE FROM livros WHERE nome = ?', [nome_remover]) #De preferencia usar uma ID para deletar algum valor, pois a ID é única para o usuário.
        self.conexao.commit()
        print(f"livro {nome_remover} foi removido com sucesso.")
    def buscar_por_nome(self, nome):
        self.cursor.execute('SELECT * FROM livros WHERE nome = ?', [nome])
        resultado = self.cursor.fetchall()
        if resultado:
            for livro in resultado:
                print(f"Encontrado: Nome {livro[0]} - Autor {livro[1]}")
        else:
            print("livro não encontrado.")
def menu():
    dao = livroDAO()
    dao.criar_tabela()
    while True:
        print("\n1 - Inserir livro")
        print("2 - Listar livros")
        print("3 - Atualizar livro")
        print("4 - Remover livro")
        print("5 - Buscar livro")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do livro: ")
            autor = input("Digite o autor do livro: ")
            dao.inserir_livro(nome, autor)
        elif opcao == "2":
            dao.listar_livro()
        elif opcao == "3":
            novo_autor = input("Digite o novo autor: ")
            nome = input("Digite o nome: ")
            dao.atualizar(nome, novo_autor)
        elif opcao == "4":
            nome_remover = input("Digite o nome do livro para remover: ")
            dao.deletar(nome_remover)
        elif opcao == "5":
            nome = input("Digite o nome do livro para buscar: ")
            dao.buscar_por_nome(nome)
        elif opcao == "6":
            dao.fechar()
            break
        else:
            print("Opção inválida.")
menu()