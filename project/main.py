from db import create_db
from reg import register_user

while True:
    create_db()
    choice = input("""Введите пункт меню:
    1. Регистрация
    2. Вход
    > """)
    if choice == '1':
        register_user()
    elif choice == '2':
        pass  # Здесь будет код для входа пользователя
