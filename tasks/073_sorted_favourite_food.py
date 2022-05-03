# Предложите пользователю ввести
# названия
# любимых блюд и сохраните их в словаре с числовыми
# индексами, начиная
# с 1. Выведите содержимое словаря
# с указанием индексов и элементов.
# Спросите пользователя, какой элемент
# он хочет исключить,
# и удалите его из
# списка. Отсортируйте оставшиеся
# данные и выведите
# содержимое словаря.

foodList = input("What is your favourite food? Use ',' to list it: ").title().split(",")
foodDict = {}
for i in foodList:
    foodDict[foodList.index(i) + 1] = i
print(foodDict)

removeFood = int(input("Enter the index of food you would like to remove: "))
del foodDict[removeFood]
print(sorted(foodDict.values()))
