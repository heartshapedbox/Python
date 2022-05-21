# Создайте двумерный список
# со стандартными индексами Python:
# предложите пользователю выбрать строку и столбец и выведите выбранное значение.

import random

list = []
for i in range(0, 4):
    nums_array = [random.randint(0, 10) for i in range(0, 3)]
    list.append(nums_array)
print(list)

row = int(input("Please, pick a row: "))
column = int(input("Please, pick a column: "))
print(list[row][column])
