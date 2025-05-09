class AnimalDAO: #falta o (banco de dados)
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE animais (
                            #falta a chave primária
                            nome TEXT
                            especie TEXT
                            )
''')