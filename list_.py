from sqlite3 import *
import sqlite3 as sql


# функция для создания кортежа
def fun(x):
    x = x.split(',')
    x[-1] = x[-1].strip()
    b =[]
    for i in x:
        if [s for s in i if s in ' ']: i = i.strip(' ')
        if [s for s in i if s in '1234567890']: i = int(i)
        b.append(i)  
    return tuple(b)

with open("users.txt","r", encoding='utf-8') as f:
        cus_file = f.readlines() 
        users = [] 
# формируем список с кортежами из файла  users.txt
        for line1 in cus_file:
                users.append(fun(line1))
print(users)

# создаем БД       
with sql.connect("btn.db") as con:
    cur = con.cursor()

    for l in users:
            cur.execute(f"""
                        INSERT INTO users(name_user, email, login, password,id_role) VALUES {l};
                    """)


