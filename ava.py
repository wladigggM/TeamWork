import os

ava = input("Введите ссылку на ваш аватар ")
print(os.getcwd())
with open(f"{ava}", "rb") as f:
    bin_file = f.read()
print(bin_file)
#print(os.getcwd())