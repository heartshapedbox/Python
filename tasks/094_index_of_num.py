# Выведите массив из пяти чисел. Предложите пользователю
# выбрать одно из них. После
# того как число будет выбрано,
# выведите его позицию в массиве. Если пользователь введет значение, отсутствующее
# в массиве, предложите ему
# выбрать снова, пока не будет
# выбрано допустимое значение.

from array import *
import random

nums_array = array ('i', [random.randint(0, 100) for i in range(0, 5)])
print(", ".join(str(i) for i in nums_array))

correct = False
while correct == False:
    num = int(input("Please, pick a number from the array: "))
    if num in nums_array:
        print(f"The index of your number is {nums_array.index(num)}.")
        correct = True
    else:
        print("Your number is out of range!")
        correct = False
