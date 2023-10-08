import sqlite3 as sql


# Класс для пользователя
class User:
    def __init__(self, name_user, email, login, password, avatar):
        self.name_user = name_user
        self.email = email
        self.login = login
        self.password = password
        self.avatar = avatar
        self.id_role = 2

    # Метод для отображения всех пользователей в базе данных
    def view_user(self):
        if self.id_role == 2:
            try:
                with sql.connect("btn.db") as con:
                    cur = con.cursor()
                    cur.execute("SELECT name_user, email, login, avatar, id_role FROM users")
                    user_data = cur.fetchall()
                    return f"{user_data}"
            except sql.Error as e:
                print("Ошибка базы данных:", e)
        elif self.id_role == 1:
            try:
                with sql.connect("btn.db") as con:
                    cur = con.cursor()
                    cur.execute("SELECT * FROM users")
                    user_data = cur.fetchall()
                    return f"{user_data}"
            except sql.Error as e:
                print("Ошибка базы данных:", e)

    # Метод для обновления инофрмации пользователя
    def update_user(self):
        name_user = input("Введите новое имя пользователя: ")
        email = input("Введите новый email пользователя: ")
        login = input("Введите новый логин пользователя: ")
        password = input("Введите новый пароль пользователя: ")
        avatar = input("Введите новый аватар пользователя: ")
        try:
            print(self.email)
            with sql.connect("btn.db") as con:
                cur = con.cursor()
                cur.execute(
                    f"UPDATE users SET name_user =?, email =?, login =?, password =?, avatar =? WHERE login =?",
                    (name_user, email, login, password, avatar, self.email))
                con.commit()
                rows_affected = cur.rowcount  # Получаем количество измененных строк
                if rows_affected > 0:
                    print(f"Обновлено {rows_affected} записей.")
                else:
                    print("Запись с таким логином не найдена.")
                print("Данные обновлены!")
        except sql.Error as e:
            print("Ошибка базы данных:", e)


# Класс для администратора
class Admin(User):
    def __init__(self, name_user, email, login, password, avatar):
        super().__init__(name_user, email, login, password, avatar)
        self.id_role = 1

    # Метод для добавления нового пользователя в базу данных
    def add_user(self, name_user, email, login, password, avatar, id_role):
        try:
            with sql.connect("btn.db") as con:
                cur = con.cursor()

                # Проверка наличия логина в базе данных
                search = cur.execute("SELECT * FROM users WHERE login =?", (login,))
                if search.fetchone() is not None:
                    print("Логин уже используется!")
                else:
                    cur.execute("""INSERT INTO users (name_user, email, login, password, avatar, id_role)
                                    VALUES (?,?,?,?,?,?)""",
                                (name_user, email, login, password, avatar, id_role))
                    print("Данные добавлены!")
        except sql.Error as e:
            print("Ошибка базы данных:", e)

    # Метод для удаления пользователя из базы данных
    def delete_user(self, login_user):
        try:
            with sql.connect("btn.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM users WHERE login =?", (login_user,))
                print("Данные удалены!")
        except sql.Error as e:
            print("Ошибка базы данных:", e)

    # Метод для обновления инофрмации пользователя
    def update_user(self):
        id_search = input("Введите id пользователя которого хотите изменить: ")
        name_user = input("Введите новое имя пользователя: ")
        email = input("Введите новый email пользователя: ")
        login = input("Введите новый логин пользователя: ")
        password = input("Введите новый пароль пользователя: ")
        avatar = input("Введите новый аватар пользователя: ")
        id_role = input("Введите новую роль пользователя: ")
        try:
            with sql.connect("btn.db") as con:
                cur = con.cursor()
                cur.execute(
                    "UPDATE users SET name_user =?, email =?, login =?, password =?, avatar =?, id_role=? WHERE id =?",
                    (name_user, email, login, password, avatar, id_role, id_search))
                print("Данные обновлены!")
        except sql.Error as e:
            print("Ошибка базы данных:", e)

    # для тестов
    def __str__(self):
        return f'{self.name_user} {self.email} {self.login} {self.password} {self.avatar}'


# Класс для заблокированного пользователя
class BlockedUser(User):
    def __init__(self, name_user, email, login, password, avatar):
        super().__init__(name_user, email, login, password, avatar)
        self.id_role = 3

    # Единственный метод для заблокированного пользователя
    def blocked_access(self):
        return 'Access blocked!'

    # Блокировал родительский метод для отображения всех пользователей в базе данных
    def view_user(self):
        return 'Access blocked!'

    def update_user(self):
        return 'Access blocked!'
# тесты
# test_user = User("test_user", "test_email", "w", "wl", "test_avatar")
# test_user.update_user()
