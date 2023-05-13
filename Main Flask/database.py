import sqlite3
from threading import Thread
# соединение с базой данных
conn = sqlite3.connect('user.db', check_same_thread=False)

def check_login_pass(login, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE login=? AND password=?", (login,password))
    data = cursor.fetchone()
    if data is None: 
        return False #если существует
    else:
        return True #если не существует
    
def add_user(login,password):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (login, password) VALUES (?,?)", (login, password))
    conn.commit()
    return True




