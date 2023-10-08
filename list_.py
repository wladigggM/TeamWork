from sqlite3 import *
import sqlite3 as sql


# функция для создания кортежа
def fun(x):
    x = x.split(',') # проходим по строке и ставим верхние кщовычки '...','...','\n'   
    x[-1] = x[-1].strip() # избавляемся от \n в конце строки
    b =[]
    count = 0
    for i in x:
        count += 1
        # удаляем пробел в начале строки если такой есть
        if [s for s in i if s in ' ']: i = i.strip(' ')
        if count == 5:
            i = int(i)
        b.append(i)  
    return tuple(b)

def mass_reg():
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
        cur.executemany(f"""INSERT INTO users(name_user, email, login, password, id_role) VALUES (?, ?, ?, ?, ?);""", users)


