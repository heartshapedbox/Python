# Спросите у пользователя, в каком направлении он хочет вести отсчет (в прямом или обратном). Если
# выбран прямой отсчет, запросите число и проведите отсчет от 1 до введенного числа. Если выбран
# обратный отсчет, запросите число меньше 20, а затем проведите обратный отсчет от 20 до заданного числа. Если введено что-то другое, выведите сообщение «I don’t understand».

countDirection = int(input("Would you like to count 1)forward or 2)backward? Enter a number: "))
if countDirection == 1:
    num = int(input("Enter some number: "))
    for i in range(1, num + 1):
        print(i)
elif countDirection == 2:
    num = int(input("Enter some number under 20: "))
    if num < 20:
        for i in range(20, num - 1, -1):
            print(i)
    else:
        print("Error! Your number doesn't match the condition.")
else:
    print("Error! Your number doesn't match the condition.")
