import sqlite3

#1-Conecta no BD
def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao

#2-Insere Dados
def insere_dados(nome, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
        '''
            INSERT INTO filmes(nome, ano,nota)
            VALUES (?, ?, ?)
        ''',(nome, ano, nota)
    )
    conexao.commit()
    conexao.close()