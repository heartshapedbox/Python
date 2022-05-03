# Введите список из десяти цветов.
# Предложите пользователю ввести
# начальное число в диапазоне от
# 0 до 4 и конечное число в диапазоне от 5 до 9. Выведите список
# цветов из интервала, заданного
# начальным и конечным числом.

colors = ["Black","White","Orange","Red","Yellow","Green","Blue","Purple","Violet","Pink"]
num1 = int(input("Please, enter a number from 0 to 4: "))
while num1 > 4:
    print("Error! Your number doesn't much the condition!")
    num1 = int(input("Please, enter a number from 0 to 4: "))
num2 = int(input("Please, enter another number from 5 to 9: "))
while num2 < 5 or num2 > 9:
    print("Error! Your number doesn't much the condition!")
    num2 = int(input("Please, enter another number from 5 to 9: "))
result = colors[num1:num2]
print(result)
