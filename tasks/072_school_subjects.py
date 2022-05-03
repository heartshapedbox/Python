# Создайте список с названиями школьных предметов. Спросите у пользователя, какие из этих предметов ему не нравятся. Удалите выбранные предметы из
# списка и выведите его повторно.

subjectsList = ["Mathematics","Biology","Chemistry","Art","Language","Technology","Physics","Health","Ecology","Astronomy"]
print(subjectsList)

removeSubject = input("\nWhat subjects above don't you like? If you have several then use ',' to list them: ").title().split(",")

for i in removeSubject:
    if i in subjectsList:
        del subjectsList[subjectsList.index(i)]

print(subjectsList)
