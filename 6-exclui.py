import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2-Exclusão
id = (1,2)
cursor.execute(
    """
    DELETE FROM filmes
    WHERE id in (?,?)
    """,
    id
)
conexao.commit()