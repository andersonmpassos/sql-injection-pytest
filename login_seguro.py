import sqlite3

def login(username, password):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    conn.close()

    return result is not None