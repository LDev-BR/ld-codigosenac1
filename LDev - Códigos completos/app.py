#---------------------- Bibliotecas --------------------------------------#
import os #Biblioteca para lidar com arquivos e diretórios
import re #Biblioteca para validações com expressões regulares (senha)
import sqlite3 #Biblioteca padrão do Python para banco de dados SQLite
from flask import flask, render_template, request, redirect, url_for, session, g  #Bibliotecas importantes do Flask
from werkzeug.utils import secure_filename #Biblioteca que garante nomes seguros para arquivos enviados
#---------------------- Configuração Inicial do App --------------------------------------#
app = flask(__name__) #Criação da aplicação Flask
app.config['SECRET_KEY'] = 'chave_luis' #Chave utilizada nas sessões
app.config['UPLOAD_FOLDER'] = 'static/uploads' #Pasta onde imagens serão salvas
app.config['MAX_CONTENT_LENGHT'] = 2 * 1024 * 1024 #Limite de upload de imagem
EXTENSOES = {'png', 'jpg', 'jpeg', 'gif'} #Extensões permitidas
DATABASE = 'users.db' #Nome do banco de dados SQLite
#---------------------- Função para Conectar o Banco --------------------------------------#
def get_db(): #Estabelecer e retornar a conexão com o banco de dados SQLite
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row #Permite acessar os dados dicionario (ex: linha['email'])
    return g.db

@app.teardown_appcontext #Automatiza a conexão
def close_db(error): #Fechar a conexão com o banco de dados após cada requisição
    db = g.pop('db', None) #Re,pve a conexão com o banco de dados g e armazena em db. Se não existir retorna None.
    if db is not None: #Se havia uma conexão, ela é fechada
        db.close
#---------------------- Função auxiliar para verificar extensão da imagem --------------------------------------#
def extensao_valida(): #Verificar se a extensão do arquivo criado é uma das permitidas
    #Verifica se o nome do arquivo possui um ponto
    #nome_arquivo.rsplit('.', 1): separa o nome do arquivo da extensão, da direita para a esquerda , uma vez uma vez só (split detecta a separação através do ponto)
    return '.' in nome_arquivo and nome_arquivo.rsplit('.', 1).lower in EXTENSOES #O '1' indica a posição do elemento a ser usado que nesse caso é a segunda pois o computador lê do 0 ao 1
#---------------------- Tabelas (Executar uma única vez)--------------------------------------#
def inicializar_banco(): #Criar as tabelas do banco caso não existam
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                            id  INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            cpf TEXT UNIQUE NOT NULL,
                            email TEXT UNIQUE NOT NULL,
                            senha TEXT NOT NULL
                                                ):
                ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS posts(
                            id  INTEGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            conteudo TEXT NOT NULL,
                            imagem  TEXT,
                            autor_id INTEGER NOT NULL,
                            FOREING_KEY (autor_id) REFERENCES usuarios (id)
            ):
    ''')
        db.commit()
#---------------------- Rota (INDEX) --------------------------------------#
@app.route('/')
def index(): #Exibir todos os posts públicos na página inicial
    db = get_db()
    posts = db.execute('''
            SELECT p.titulo, p.conteudo, u.nome 
            FROM posts p
            JOIN usuarios u ON p.autor_id = u.id
''') #p é apelido para posts e u = usuários

#---------------------- Rotas--------------------------------------#
#---------------------- Rotas--------------------------------------#
#---------------------- Rotas--------------------------------------#