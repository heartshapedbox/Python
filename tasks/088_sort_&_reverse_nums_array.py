# Предложите пользователю ввести пять
# целых чисел и сохраните их в массиве.
# Отсортируйте список и выведите его содержимое в обратном порядке.
from array import *

numArray = array ("i", [])
prompt = int(input("How many numbers would you like to use? "))

while prompt != 0:
    num = int(input("Enter a number: "))
    numArray.append(num)
    prompt -= 1

numArray = sorted(numArray)
numArray.reverse()
print(numArray)
