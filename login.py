import sqlite3 as sql
from UsersRole import *


# Функция для вход

def login_user():
    login = input("Введите логин пользователя: ")
    password = input("Введите пароль пользователя: ")

    try:
        with sql.connect("btn.db") as con:
            cur = con.cursor()

            # Проверка наличия логина в базе данных
            cur.execute("SELECT * FROM users WHERE login =?", (login,))
            search_user_data = cur.fetchone()
            if search_user_data is None:
                print("Логин не найден!")
            else:
                # Проверка пароля
                if search_user_data[4] == password:
                    print("Вы успешно авторизовались!")
                    role = search_user_data[6]
                    return role
                else:
                    print("Пароль не совпадает!")
    except sql.Error as e:
        print("Ошибка базы данных:", e)