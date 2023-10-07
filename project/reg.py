import os

full_name = 'Chelovek Admin Team'
email = 'admin@reglog.com'
login = 'admin'
password = 'admin'
avatar = ''
role = 'admin'

if os.path.exists('users'):
    print("Папка users уже существует!")
    os.chdir('users')

    if os.path.exists('login.txt') and os.path.exists('password.txt'):
        print("Файлы уже существуют!")
        with open('login.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if login == line:
                    print("Логин уже используется!")
                    break
            else:  # Этот блок выполняется, если логин не найден в файле
                with open('login.txt', 'a+') as f:
                    f.write(login + '\n')
                with open('password.txt', 'a+') as f:
                    f.write(f'{login}: {password}\n')
    else:
        with open('login.txt', 'w') as f:
            f.write(login + '\n')
        with open('password.txt', 'a+') as f:
            f.write(f'{login}: {password}\n')
else:
    os.mkdir('users')
