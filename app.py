from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

# Conexão com o banco de dados
engine = create_engine("mysql+pymysql://root:Sasa35794hit?@localhost:3306/biblioteca")  # troca sua senha aqui
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Tabela de usuários
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))

# Tabela de livros
class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    autor = Column(String(100))
    disponivel = Column(String(3), default='sim')  # sim ou nao

# Tabela de empréstimos
class Emprestimo(Base):
    __tablename__ = 'emprestimos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    livro_id = Column(Integer, ForeignKey('livros.id'))
    data_emprestimo = Column(DateTime, default=datetime.now)
    data_devolucao = Column(DateTime, nullable=True)

    usuario = relationship("Usuario")
    livro = relationship("Livro")

    

# Criar as tabelas no banco
Base.metadata.create_all(engine)

print("Tabelas criadas com sucesso!")
