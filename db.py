import sqlite3 as sql


# Функция создания базы данных
def create_db():
    with sql.connect("btn.db") as con:
        cur = con.cursor()

        # создаем таблицу с ролью
        cur.executescript("""
                    CREATE TABLE IF NOT EXISTS roles(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role VARCHAR(20) NOT NULL);
                    """)

        # создаем таблицу с пользователями
        cur.executescript("""
                    CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_user VARCHAR(200) NOT NULL,
                    email VARCHAR(200) UNIQUE NOT NULL,
                    login VARCHAR(200) UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    avatar BLOB,
                    id_role INTEGER NOT NULL,
                    FOREIGN KEY (id_role) REFERENCES roles(id));
                    """)
        # Проверяем наличие ролей в базе данных
        searcher = cur.execute("""SELECT * FROM roles""")
        if searcher.fetchone() is None:
            cur.execute("""
                        INSERT INTO roles (role) VALUES 
                        ('Администратор'),
                        ('Пользователь'),
                        ('Заблокированный')
                            """)
