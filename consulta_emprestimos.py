from app import session, Usuario, Livro, Emprestimo

# Consulta todos os empréstimos ainda não devolvidos
resultados = (
    session.query(Usuario.nome, Livro.titulo, Emprestimo.data_emprestimo)
    .join(Emprestimo, Usuario.id == Emprestimo.usuario_id)
    .join(Livro, Livro.id == Emprestimo.livro_id)
    .filter(Emprestimo.data_devolucao == None)
    .all()
)

if resultados:
    for nome, titulo, data in resultados:
        print(f"{nome} pegou o livro '{titulo}' em {data.strftime('%d/%m/%Y %H:%M')}")
else:
    print("Nenhum livro emprestado no momento.")
