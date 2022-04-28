# Предложите пользователю ввести имя и фамилию в нижнем
# регистре. Преобразуйте строки к титульному регистру и соедините их. Выведите полученный результат

name = input("Hello! Enter your name in lowercase, please: ").title()
surname = input("Enter your surname in lowercase, please: ").title()
fullName = name + " " surname
print(fullName)
