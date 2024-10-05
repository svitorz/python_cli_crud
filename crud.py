from db import get_connection


def create_table():
    conn = get_connection()
    if conn is None:
        return
    cursor = conn.cursor()

    try:
        cursor.execute(
            "CREATE TABLE USERS(id_users serial PRIMARY KEY,name varchar(50),email varchar(150) UNIQUE,senha varchar(255));"
        )

        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        if 'relation "users" already exists' in str(e):
            return True
        else:
            return e


def list_users():
    conn = get_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name,id_users FROM users;")
        users = cursor.fetchall()

        cursor.close()
        conn.close()

        return users
    except Exception as e:
        print("Erro ao retornar usuários", e)
        return []
