# Предложите пользователю ввести число
# с большим количеством знаков в дробной
# части. Умножьте это число на 2 и выведите результат с точностью до двух знаков
# в дробной части..

num = float(input("Please, enter a number with a lot of decimal places: "))
num = round(num * 2, 2)
print(num)
