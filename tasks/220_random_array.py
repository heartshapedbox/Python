# Создайте массив, содержащий
# пять рандомных чисел. Если в массиве есть повторяющиеся числа,
# выведите это число, сколько раз оно повтояется и сам массив (или все числа массива).
# Если в массиве нет повторяющихся чисел - генерируйте новый
# массив с рандомными числами.

from array import *
import random

result = False
while result == False:
    nums = array ("i", [])
    for i in range(0, 5):
        num = random.randint(0, 100)
        nums.append(num)

    rangeStart = 1
    length = len(nums)

    for i in range(0, length):
        if nums[i] in nums[rangeStart:length]:
            print(", ".join(str(i) for i in nums))
            print(f"Number {nums[i]} has been repeated {nums.count(nums[i])} times.")
            result = True
            break
        else:
            rangeStart += 1
        result = False
