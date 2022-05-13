# Предложите пользователю ввести пять
# целых чисел и сохраните их в массиве.
# Отсортируйте список и выведите его содержимое в обратном порядке.
from array import *
array = ('i', [])

# prompt = int(input("How many numbers would you like to use? "))
for i in range(0, 5):
    num = int(input("Enter a number: "))
    array.append(num)

array = sorted(array)
array.reverse()
print(array)
