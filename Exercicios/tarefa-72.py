import sqlite3
class conexaoBanco:
    def __init__(self, nome_banco = "cursos.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class cursoDAO(conexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cursos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            nivel TEXT CHECK(nivel IN ('Básico', 'Intermediário', 'Avançado')) NOT NULL
            )
    ''')
    def inserir_curso(self, nome, nivel):
        self.cursor.execute('''
            INSERT INTO cursos (nome, nivel) VALUES (?, ?)
    ''', (nome, nivel))
        self.conexao.commit()
        print(f"{nome} de {nivel} inserido com sucesso.")
    def listar_curso(self):
        self.cursor.execute('SELECT * FROM cursos')
        cursos = self.cursor.fetchall()
        print("\nLista de cursos: ")
        for curso in cursos:
            print(f"ID: {curso[0]} - Nome do curso: {curso[1]} - nivel: {curso[2]}")
def menu():
    dao = cursoDAO()
    dao.criar_tabela()
    while True:
        print("\n1 - Inserir curso")
        print("2 - Listar cursos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do curso: ")
            print("Escolha o nível do curso")
            while True:
                print("1 - Básico")
                print("2 - Intermediário")
                print("3 - Avançado")
                opcao1 = input("Escolha sua opção: ")
                if opcao1 == "1":
                    dao.inserir_curso(nome, "Básico")
                    break
                elif opcao1 == "2":
                    dao.inserir_curso(nome, "Intermediário")
                    break
                elif opcao1 == "3":
                    dao.inserir_curso(nome, "Avançado")
                    break
                else:
                    print("Escolha uma opção válida")
        elif opcao == "2":
            dao.listar_curso()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Opção inválida.")
menu()