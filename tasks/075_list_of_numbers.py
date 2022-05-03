# Создайте список из четырех трехзначных чисел. Выведите содержимое списка, при этом каждый
# элемент должен выводиться на
# отдельной строке. Предложите
# пользователю ввести число из трех
# цифр. Если введенное число совпадает с одним из чисел в списке,
# выведите позицию этого числа;
# в противном случае выведите сообщение «That is not in the list».

numbers = [199,277,623,592]
for i in numbers:
    print(i)

num = int(input("Please, enter a 3 digits number: "))
if num in numbers:
    print(numbers.index(num))
else:
    print("That is not in the list!")
