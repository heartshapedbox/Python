# Присвойте переменной с именем total значение 0. Предложите
# пользователю ввести пять чисел, и после каждого ввода спрашивайте, хочет ли он включить это число в суммирование. Если ответ будет
# положительным, прибавьте введенное число к total. Если же ответ
# будет отрицательным, число к total не прибавляется. После ввода
# всех пяти чисел выведите значение total.

total = 0
for i in range(0, 5):
    num = int(input("Enter some number: "))
    prompt = input("Would you like this number to be included in addition operation? (y/n): ").lower()
    if prompt == "y":
        total += num
    else:
        total += 0
print(f"The result is {total}.")
