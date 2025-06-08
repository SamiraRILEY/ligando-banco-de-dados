from app import session, Usuario, Livro

# Cadastrar um usuário
usuario1 = Usuario(nome="Tatiana", email="tatiana@email.com")
session.add(usuario1)

# Cadastrar um livro
livro1 = Livro(titulo="1984", autor="George Orwell")
session.add(livro1)

# Salvar no banco
session.commit()

print("Usuário e livro cadastrados com sucesso!")
