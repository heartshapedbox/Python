# Предложите пользователю ввести пять
# целых чисел и сохраните их в массиве.
# Отсортируйте список и выведите его содержимое в обратном порядке.
from array import *

num_array = array ("i", [])
prompt = int(input("How many numbers would you like to use? "))

while prompt != 0:
    num = int(input("Enter a number: "))
    num_array.append(num)
    prompt -= 1

num_array = sorted(num_array)
num_array.reverse()
print(num_array)
