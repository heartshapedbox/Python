# Предложите пользователю ввести радиус круга (расстояние от центра до внешней границы.) Вычислите
# площадь круга (π * радиус2).

import math
radius = int(input("Please, enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print(area)
