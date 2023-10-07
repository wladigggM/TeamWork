from sqlite3 import *
import sqlite3 as sql

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
    
    
    # cur.execute("""
    #             INSERT INTO roles (role) VALUES 
    #             ('Администратор'),
    #             ('Пользователь'),
    #             ('Заблокированный')
    #                 """)

    # Создаем админа
    # cur.execute("""
    #             INSERT INTO `users`(`name_user`, `email`, `login`, `password`,`id_role`) VALUES 
    #             ('Админ','admin@btn.ru','admin','admin1234','1');
    #                  """)

    # показать все роли
    res = cur.execute("""SELECT * FROM `roles`""")
    for row in res.fetchall(): 
        print(row) 

    print(cur.execute("""SELECT * FROM `users`""").fetchall())

