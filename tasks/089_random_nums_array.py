# Создайте массив для хранения целых чисел. Сгенерируйте пять случайных чисел и сохраните их в массиве.
# Выведите массив (каждый элемент должен выводиться в отдельной строке).

from array import *
import random

nums_array = array ("i", [])

start = 0
while start != 5:
    random_num = random.randint(0, 100)
    nums_array.append(random_num)
    start += 1

for i in nums_array:
    print(i)
