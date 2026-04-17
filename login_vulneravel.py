import sqlite3

def login(username, password):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM usuarios WHERE username = '{username}' AND password = '{password}'"
    
    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()

    return result is not None