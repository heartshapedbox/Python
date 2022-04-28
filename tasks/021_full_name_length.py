# Предложите пользователю ввести сначала имя,
# а затем фамилию. Соедините их, разделив пробелом, после чего выведите полное имя и его
# длину

name = input("Hello! Enter your name, please: ")
surname = input("Enter your surname, please: ")
fullName = name + " " + surname
print(len(fullName))
