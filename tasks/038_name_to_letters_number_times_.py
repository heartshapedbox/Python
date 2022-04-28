# Предложите пользователю ввести имя и число. Выведите
# имя (по одной букве
# в каждой строке) и повторите вывод равное
# введенному числу количество раз.

name = input("Please, enter your name: ")
num = int(input("Please, enter some number: "))
for i in range(0, num):
    for i in name:
        print(i)
