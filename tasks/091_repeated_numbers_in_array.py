# Создайте массив, содержащий
# пять чисел (два из которых
# должны повторяться). Выведите весь массив. Предложите
# пользователю ввести одно из
# чисел массива, после чего выведите сообщение, в котором
# указано, сколько раз число
# встречается в этом массиве.

from array import *

nums_array = array ('i', [3,3,5,27,13])
print(", ".join(str(i) for i in nums_array))

num = int(input("Please, enter a number from the array above: "))
if nums_array.count(num) > 1:
    print(f"Number {num} has been repeated {nums_array.count(num)} times.")
else:
    print(f"Number {num} has been repeated {nums_array.count(num)} time.")
