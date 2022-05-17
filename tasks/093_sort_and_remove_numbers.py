# Предложите пользователю
# ввести пять чисел. Отсортируйте их и выведите для
# пользователя. Предложите выбрать одно из чисел. Удалите
# выбранное число из исходного
# массива и сохраните его
# в новом

from array import *

nums_array = sorted(array ('i', [int(input("Enter a number: ")) for i in range(0, 5)]))
print(",".join(str(i) for i in nums_array))

removed_num = int(input("Pick a number: "))
nums_array.remove(removed_num)
print(",".join(str(i) for i in nums_array))

new_nums_array = array ('i', [removed_num])
print("".join(str(i) for i in new_nums_array))
