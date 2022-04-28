# Предложите пользователю ввести радиус
# и высоту цилиндра. Вычислите его объем
# (площадь круга * высота) и выведите его
# с точностью до трех знаков.

import math
radius = int(input("Please, enter the radius of the cylinder: "))
height = int(input("Please, enter the height of the cylinder: "))
circleArea = math.pi * (radius ** 2)
cylinderVolume = circleArea * height
result = round(cylinderVolume, 2)
print(result)
