# Предложите пользователю ввести сначала одно число, а затем другое. Сложите два числа
# и спросите, хочет ли он прибавить еще одно. Если он введет
# «y», предложите ввести еще одно
# число; это продолжается до тех
# пор, пока пользователь не введет
# ответ «y». После того как цикл
# остановится, выведите сумму

num1 = int(input("Please, enter some number: "))
num2 = int(input("Please, enter another number: "))
sum = num1 + num2
prompt = input("Would you like to enter another number? (y/n): ").lower()
if prompt == "y":
    while prompt == "y":
        num = int(input("Please, enter a number: "))
        sum += num
        prompt = input("Would you like to enter another number? (y/n): ").lower()
    print(f"The sum is {sum}.")
else:
    print(f"The sum is {sum}.")
