import sqlite3
def save_user(name, age):
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO users (name,age) VALUES (?,?)",("Alice",30))
    conn.commit()
    conn.close()