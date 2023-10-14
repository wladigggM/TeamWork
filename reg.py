import sqlite3 as sql
from UsersRole import *


# Функция для создания админа
def create_admin():
    try:
        with sql.connect("btn.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM users")
            if cur.fetchone() is None:
                cur.execute("""
                INSERT INTO users(name_user, email, login, password, avatar, id_role) VALUES
                ('admin_name','admin@btn.ru','admin','adminpass', 'admin.png', '1');
                """)
                print('Администратор успешно создан!')
    except sql.Error as e:
        print("Ошибка базы данных:", e)


# Функция для регистрации пользователя
def register_user():
    name_user = input("Введите имя пользователя: ")
    email = input("Введите email пользователя: ")
    login = input("Введите логин пользователя: ")
    password = input("Введите пароль пользователя: ")
    avatar = input("Введите путь до аватарки: ")
    id_role = 2
    try:
        with sql.connect("btn.db") as con:
            cur = con.cursor()

            # Проверка наличия логина в базе данных
            search = cur.execute("SELECT * FROM users WHERE login = ?", (login,))
            if search.fetchone() is not None:
                print("Логин уже используется!")
            else:
                cur.execute("""INSERT INTO users (name_user, email, login, password, avatar, id_role)
                                VALUES (?, ?, ?, ?, ?, ?)""",
                            (name_user, email, login, password, added_avatar(avatar), id_role))
                print("Данные добавлены!")
                con.commit()
    except sql.Error as e:
        print("Ошибка базы данных:", e)
