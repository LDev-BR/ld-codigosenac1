import sqlite3
class conexaoBanco:
    def __init__(self, nome_banco = "visitantes.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.conexao.close()
class visitanteDAO(conexaoBanco): # DAO - Data Acess Object
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS visitantes(
                            nome TEXT NOT NULL,
                            motivo TEXT NOT NULL
            )
    ''')
    def inserir_visitante(self, nome, motivo):
        self.cursor.execute('''
            INSERT INTO visitantes (nome, motivo) VALUES (?, ?)
    ''', (nome, motivo))
        self.conexao.commit()
        print(f"{nome} de {motivo} inserido com sucesso.")
    def listar_visitante(self):
        self.cursor.execute('SELECT * FROM visitantes')
        visitantes = self.cursor.fetchall()
        print("\nLista de visitantes: ")
        for visitante in visitantes:
            print(f"Nome do visitante: {visitante[0]} - motivo: {visitante[1]}")
    def atualizar(self, nome, novo_motivo):
        self.cursor.execute('UPDATE visitantes SET motivo = ? WHERE nome = ?', (novo_motivo, nome))
        self.conexao.commit()
        print(f"motivo de {nome} atualizada para {novo_motivo}")
    def deletar(self, nome_remover):
        self.cursor.execute('DELETE FROM visitantes WHERE nome = ?', [nome_remover]) #De preferencia usar uma ID para deletar algum valor, pois a ID é única para o usuário.
        self.conexao.commit()
        print(f"Visitante {nome_remover} foi removido com sucesso.")
def menu():
    dao = visitanteDAO()
    dao.criar_tabela()
    while True:
        print("\n1 - Inserir visitante")
        print("2 - Listar visitantes")
        print("3 - Atualizar visitante")
        print("4 - Remover visitante")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do visitante: ")
            motivo = input("Digite o motivo do visitante: ")
            dao.inserir_visitante(nome, motivo)
        elif opcao == "2":
            dao.listar_visitante()
        elif opcao == "3":
            novo_motivo = input("Digite o novo motivo: ")
            nome = input("Digite o nome: ")
            dao.atualizar(nome, novo_motivo)
        elif opcao == "4":
            nome_remover = input("Digite o nome do visitante para remover: ")
            dao.deletar(nome_remover)
        elif opcao == "5":
            dao.fechar()
            break
        else:
            print("Opção inválida.")
menu()