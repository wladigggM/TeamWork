import sqlite3 as sql


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
                print("\nЛогин не найден!\n")
            else:
                # Проверка пароля
                if search_user_data[4] == password:
                    print("\nВы успешно авторизовались!\n")
                    role = search_user_data[6]
                    return role
                else:
                    print("\nПароль не совпадает!\n")
    except sql.Error as e:
        print("\nОшибка базы данных:\n", e)


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


# функция для создания кортежа
def fun(x):
    x = x.split(',')  # проходим по строке и ставим верхние кщовычки '...','...','\n'
    x[-1] = x[-1].strip()  # избавляемся от \n в конце строки
    b = []
    count = 0
    for i in x:
        count += 1
        # удаляем пробел в начале строки если такой есть
        if [s for s in i if s in ' ']: i = i.strip(' ')
        if count == 5:
            i = int(i)
        b.append(i)
    return tuple(b)


# функция массовой регистрации из файла
def mass_reg(file):
    with open(file, "r", encoding='utf-8') as f:
        cus_file = f.readlines()
        users = []
        # формируем список с кортежами из файла  users.txt
    for line1 in cus_file:
        users.append(fun(line1))
    print(users)

    # создаем БД
    with sql.connect("btn.db") as con:
        cur = con.cursor()
        cur.executemany(f"""INSERT INTO users(name_user, email, login, password, id_role) VALUES (?, ?, ?, ?, ?);""",
                        users)


def added_avatar(avatar):
    with open(avatar, "rb") as f:
        bin_file = f.read()
        return bin_file
