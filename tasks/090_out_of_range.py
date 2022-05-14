# Предложите пользователю вводить целые числа. Если пользователь вводит число от 10 до 20, сохраните его в массиве;
# в противном случае выведите сообщение «Outside the range».
# После того как пять чисел будут успешно добавлены в массив,
# выведите сообщение «Thank you» и выведите массив, каждый
# элемент которого находился бы на отдельной строке.

from array import *

nums_array = array ("i", [])

while len(nums_array) != 5:
    num = int(input("Enter a number: "))
    if num >= 10 and num <= 20:
        nums_array.append(num)
    else:
        print("Out of range!")

print("Thank you!")
for i in nums_array:
    print(i)
