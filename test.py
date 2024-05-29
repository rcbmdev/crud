from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1- Criando a conexão com o banco de dados
engine = create_engine('sqlite:///x.db', echo=True)

# Base para as classes do modelo
Base = declarative_base()

# Classe para a tabela 'filmes'
class Filme(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

# Criação da tabela
Base.metadata.create_all(engine)

# # Função para adicionar um filme ao banco de dados
def adicionar_filme(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = Filme(nome=nome, ano=ano, nota=nota)
    session.add(filme)
    session.commit()
    session.close()

# # Exemplo de uso: Adicionando um filme
# adicionar_filme('Filme Teste2', 2025, 9.5)

def atualizar_filme(filme_id, nome=None, ano=None, nota=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=filme_id).first()
    filme.nome = nome
    filme.ano = ano
    filme.nota = nota
    session.commit()
    session.close()

def excluir_filme(filme_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=filme_id).first()
    session.delete(filme)
    session.commit()
    session.close()

# atualizar_filme(1, nome="Novo Nome", ano=2024, nota=8.0)
excluir_filme(1)
print("Tabela foi criada e filme adicionado com sucesso!")
