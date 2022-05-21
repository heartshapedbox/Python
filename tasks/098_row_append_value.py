# Создайте двумерный список
# со стандартными индексами Python:
# предложите пользователю выбрать строку и выведите
# только ее. Предложите ввести новое значение, добавьте его в конец строки, после чего снова выведите
# измененную строку.

import random

list = []
for i in range(0, 4):
    random_list = [random.randint(1, 10) for i in range(0, 3)]
    list.append(random_list)
print(list)

row = int(input("Please, pick a row: "))
print(list[row])

value = int(input("Please, enter a new value: "))
list[row].append(value)
print(list[row])
