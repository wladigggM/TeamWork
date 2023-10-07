import sqlite3 as sql


class User:
    def __init__(self, name_user, email, login, password, avatar):
        self.name_user = name_user
        self.email = email
        self.login = login
        self.password = password
        self.avatar = avatar
        self.id_role = 2

    def view_user(self):
        if self.id_role == 2:
            return f"""
            id: {self.id}
            name_user: {self.name_user}
            email: {self.email}
            login: {self.login}
            password: Access closed
            avatar: {self.avatar}"""
        elif self.id_role == 1:
            return f"""
            id: {self.id_role}
            name_user: {self.name_user}
            email: {self.email}
            login: {self.login}
            password: {self.password}
            avatar: {self.avatar}"""


class Admin(User):
    def __init__(self, name_user, email, login, password, avatar):
        super().__init__(name_user, email, login, password, avatar)
        self.id_role = 1

    def add_user(self, name_user, email, login, password, avatar, id_role):
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
                con.commit()

    def delete_user(self, login_user):
        with sql.connect("btn.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE login =?", (login_user,))

    def update_user(self, name_user, email, login, password, avatar, id_role):
        with sql.connect("btn.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE users SET name_user =?, email =?, login =?, password =?, avatar =? WHERE id =?",
                        (name_user, email, login, password, avatar))

    def __str__(self):
        return self.name_user + self.email + self.login + self.password + self.avatar


class BlockedUser(User):
    def __init__(self, name_user, email, login, password, avatar):
        super().__init__(name_user, email, login, password, avatar)
        self.id_role = 3

    def blocked_access(self):
        return 'Access blocked!'

    def view_user(self):
        return 'Access blocked!'
