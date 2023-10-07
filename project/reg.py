import sqlite3 as sql


# Функция для регистрации пользователя
def register_user():
    name_user = input("Введите имя пользователя: ")
    email = input("Введите email пользователя: ")
    login = input("Введите логин пользователя: ")
    password = input("Введите пароль пользователя: ")
    avatar = input("Введите аватар пользователя: ")
    id_role = input("Введите роль пользователя: ")

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
                            (name_user, email, login, password, avatar, id_role))
                print("Данные добавлены!")
                con.commit()
    except sql.Error as e:
        print("Ошибка базы данных:", e)
