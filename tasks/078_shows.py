# Создайте список с названиями четырех телевизионных
# передач и выведите их на отдельных строках. Предложите
# пользователю ввести название
# еще одной передачи и позицию,
# на которой она должна быть
# вставлена в список. Снова выведите список, в котором все
# пять передач находятся на новых позициях.

shows = ["SNL","Conan","Talking Dead","Tonight Show"]
for i in shows:
    print(i)

prompt = input("\nPlease, enter another show and position in the list. Using ',': ")
anotherShow = prompt.split(",")[0]
anotherShowIndex = prompt.split(",")[1]
shows.insert(int(anotherShowIndex), anotherShow)
for i in shows:
    print(i)
