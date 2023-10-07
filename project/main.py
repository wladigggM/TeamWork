from db import create_db
from reg import register_user
from UsersRole import *
from login import login_user

while True:
    create_db()
    choice = input("""Введите пункт меню:
    1. Регистрация
    2. Вход
    > """)

    if choice == '1':
        register_user()
    elif choice == '2':
        role = login_user()
        if role == 1:
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
            5. Выход
            > """)
            if choice == '1':
                admin.view_user()
