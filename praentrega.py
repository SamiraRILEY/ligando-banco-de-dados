class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    autor = Column(String(100))

class Emprestimo(Base):
    __tablename__ = 'emprestimos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    livro_id = Column(Integer, ForeignKey('livros.id'))
    data_emprestimo = Column(DateTime)
    data_devolucao = Column(DateTime)
