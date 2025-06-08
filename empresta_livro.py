from app import session, Emprestimo

# Criar empréstimo (usuário com ID 1 pega livro com ID 1)
novo_emprestimo = Emprestimo(usuario_id=1, livro_id=1)

# Adiciona e salva
session.add(novo_emprestimo)
session.commit()

print("Livro emprestado com sucesso!")
