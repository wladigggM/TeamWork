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
        customers = [] 
# формируем список с кортежами из файла  users.txt
        for line1 in cus_file:
                customers.append(fun(line1))
print(customers)


