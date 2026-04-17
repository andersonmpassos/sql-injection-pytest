from login_seguro import login
from banco import criar_tabela

def test_sql_injection_bloqueado():
    criar_tabela()

    usuario = "admin' --"
    senha = "123"

    assert login(usuario, senha) == False