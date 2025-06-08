from app import session, Emprestimo
from datetime import datetime

# Busca o empréstimo (pega o primeiro da tabela)
emprestimo = session.query(Emprestimo).filter(Emprestimo.data_devolucao == None).first()

if emprestimo:
    emprestimo.data_devolucao = datetime.now()
    session.commit()
    print("Livro devolvido com sucesso!")
else:
    print("Nenhum empréstimo pendente encontrado.")
