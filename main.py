from db import create_db
from reg import register_user
from reg import create_admin
from UsersRole import *
from login import login_user
from time import sleep
from list_ import mass_reg

while True:
    create_db()
    create_admin()
    choice = input("""Введите пункт меню:
    1. Регистрация
    2. Вход
    3. ВЫЙТИ
    > """)

    if choice == '1':
        register_user()
    elif choice == '2':
        role = login_user()
        if role == 1:
            while True:
                with sql.connect("btn.db") as con:
                    cur = con.cursor()
                    cur.execute("SELECT * FROM users WHERE id_role = 1")
                    admin_data = cur.fetchone()
                    admin = Admin(admin_data[1], admin_data[1], admin_data[2], admin_data[3], admin_data[4])
                    choice = input("""Введите пункт меню:
                    1. Пользователи
                    2. Добавить пользователя
                    3. Удалить пользователя
                    4. Изменить пользователя
                    5. Массовая регистрация
                    6. Выход
                    > """)
                    if choice == '1':
                        print(admin.view_user())
                    elif choice == '2':
                        admin.add_user(input("Введите имя пользователя: "), input("Введите email пользователя: "),
                                       input("Введите логин пользователя: "), input("Введите пароль пользователя: "),
                                       input("Добавьте аватар пользователя:"), input("Укажите роль пользователя:"))
                    elif choice == '3':
                        admin.delete_user(input("Введите логин пользователя которого хотите удалить: "))
                    elif choice == '4':
                        admin.update_user()
                    elif choice == '5':
                        file = 'users.txt'
                        mass_reg(file)
                    elif choice == '6':
                        role = 0
                        break
        if role == 2:  # Дописать действия для простого пользователя
            while True:
                with sql.connect("btn.db") as con:
                    cur = con.cursor()
                    cur.execute("SELECT * FROM users WHERE id_role = 2")
                    user_data = cur.fetchone()
                    user = User(user_data[1], user_data[2], user_data[3], user_data[4], user_data[5])
                    choice = input("""Введите пункт меню:
                    1. Пользователи
                    2. Отредактировать свои данные
                    3. Выход
                    > """)
                    if choice == '1':
                        print(user.view_user())
                    elif choice == '2':
                        user.update_user()
                    elif choice == '3':
                        role = 0
                        break
        if role == 3:  # Дописать действия для заблокированного пользователя
            while True:
                with sql.connect("btn.db") as con:
                    cur = con.cursor()
                    cur.execute("SELECT * FROM users WHERE id_role = 2")
                    blocked_data = cur.fetchone()
                    blocked_user = BlockedUser(blocked_data[1], blocked_data[1], blocked_data[2], blocked_data[3],
                                               blocked_data[4])
                    choice = input("""Введите пункт меню:
                    1. Пользователи
                    2. Отредактировать свои данные
                    3. Выход
                    > """)
                    if choice == '1':
                        print(blocked_user.view_user())
                        sleep(1)
                    elif choice == '2':
                        print(blocked_user.update_user())
                        sleep(1)
                    elif choice == '3':
                        role = 0
                        break
    elif choice == '3':
        break
