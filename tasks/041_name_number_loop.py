# Предложите пользователю ввести имя и число.
# Если число меньше 10,
# программа должна вывести имя заданное количество раз; в противном случае она выводит
# сообщение «Too high»
# три раза.

name = input("Please, enter your name: ")
num = int(input("Please, enter some number: "))
if num < 10:
    for i in range(0, num):
        print(name)
else:
    for i in range(0, 3):
        print("Too high!")
