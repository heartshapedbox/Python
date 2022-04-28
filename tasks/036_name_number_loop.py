# Предложите пользователю ввести имя имя и число, а затем вывести имя заданное
# количество раз.

name = input("Please, enter your name: ")
num = int(input("Please, enter some number: "))
for i in range(0, num):
    print(name)
