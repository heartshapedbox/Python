# Выведите следующее сообщение:
# 1) Square
# 2) Triangle
# Enter a number:
# Если пользователь вводит 1, программа запрашивает
# длину стороны квадрата и выводит его площадь. Если
# пользователь вводит 2, программа запрашивает длину
# стороны и высоту треугольника, проведенную к этой
# стороне, после чего выводит его площадь. Если пользователь вводит что-то другое, программа должна выдать подходящее сообщение об ошибке.

print("1) Square\n2) Triangle\n")
num = int(input("Enter a number: "))
if num == 1:
    sideLength = int(input("Enter the length of the side: "))
    print(sideLength ** 2)
elif num == 2:
    sideLength = int(input("Enter the length of the side: "))
    height = int(input("Enter the height: "))
    print((sideLength * height) / 2)
else:
    print("Error!")
