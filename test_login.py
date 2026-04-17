from login_seguro import login

def test_sql_injection_bloqueado():
    usuario = "admin' --"
    senha = "123"

    assert login(usuario, senha) == False