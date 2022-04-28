# Предложите пользователю ввести имя. Если длина имени
# меньше 5 символов, предложите ввести фамилию, соедините
# их (без пробела) и выведите полное имя в верхнем регистре.
# Если длина имени составляет 5 и более символов, выведите
# имя в нижнем регистре.

name = input("Please, enter your name: ").lower()
if len(name) < 5:
    surname = input("Please, enter your surname: ").lower()
    fullName = name + surname
    print(fullName.upper())
else:
    print(fullName.lower())
