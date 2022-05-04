# Создайте пустой список с именем nums. Предложите пользователю последовательно
# вводить числа. После ввода
# каждого числа добавьте его
# в конец списка nums и выведите список. После того как
# пользователь введет три числа,
# спросите, хочет ли он оставить
# последнее введенное число
# в списке. Если пользователь ответит «no», удалите последний
# элемент из списка. Выведите
# список.

nums = []
while len(nums) < 3:
    num = int(input("Please, enter a nubmer: "))
    nums.append(num)
    print(nums)
prompt = input("Would you like to keep the last number? (y/n) ").lower()
if prompt == "n":
    nums.remove(num)
    print(nums)
else:
    print(nums)
