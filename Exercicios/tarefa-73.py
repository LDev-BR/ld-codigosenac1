import sqlite3
class conexaoBanco:
    def __init__(self, nome_banco = "professores.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.conexao.close()
class professorDAO(conexaoBanco): # DAO - Data Acess Object
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS professores(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            disciplina TEXT NOT NULL
            )
    ''')
    def inserir_professor(self, nome, disciplina):
        self.cursor.execute('''
            INSERT INTO professores (nome, disciplina) VALUES (?, ?)
    ''', (nome, disciplina))
        self.conexao.commit()
        print(f"{nome} de {disciplina} inserido com sucesso.")
    def listar_professor(self):
        self.cursor.execute('SELECT * FROM professores')
        professores = self.cursor.fetchall()
        print("\nLista de professores: ")
        for professor in professores:
            print(f"ID: {professor[0]} - Nome do professor: {professor[1]} - disciplina: {professor[2]}")
def menu():
    dao = professorDAO()
    dao.criar_tabela()
    while True:
        print("\n1 - Inserir professor")
        print("2 - Listar professores")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do professor: ")
            disciplina = input("Digite o disciplina do professor: ")
            dao.inserir_professor(nome, disciplina)
        elif opcao == "2":
            dao.listar_professor()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Opção inválida.")
menu()