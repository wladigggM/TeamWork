

ava = input("Введите ссылку на ваш аватар ")

with open(ava, "rb") as f:
    bin_file = f.read()
print(bin_file)
