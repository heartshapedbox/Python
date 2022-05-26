# Выведите следующее меню:
# 1) Create a new file
# 2) Display the file
# 3) Add a new item to the file
# Make a selection 1, 2 or 3: Предложите пользователю выбрать один из вариантов. Если пользователь введет что-либо, кроме 1, 2 и 3, программа должна вывести соответствующее сообщение об ошибке. Если пользователь выберет 1, предложите ему ввести название школьного предмета и сохраните его в новом файле с именем Subject.txt. Существующий файл с таким именем должен быть заменен новым файлом. Если пользователь выберет 2, выводится содержимое файла Subject.txt. Если пользователь выберет 3, предложите пользователю ввести новый предмет, сохраните его в файле, а затем выведите все его содержимое. Запустите программу несколько раз, чтобы протестировать разные команды.

import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')
file = open('Subject.txt', 'w')
file.write('Subjects:\n')
file.write('Art\n')
file.write('Mathematics\n')
file.write('Science\n')
file.close()

print('1) Create a new file\n2) Display the file\n3) Add a new item to the file\n')
option = int(input("Please, select an option (1, 2 or 3): "))

if option == 1:
    subject = input("Please, enter some school subject: ").title()
    file = open('Subject.txt', 'w')
    file.write(subject)
elif option == 2:
    file = open('Subject.txt', 'r')
    print(file.read())
    file.close()
elif option == 3:
    subject = input("Please, enter some school subject: ").title()
    file = open('Subject.txt', 'a')
    file.write(subject)
    file.close()
    file = open('Subject.txt', 'r')
    print(file.read())
    file.close()
else:
    print("Error. You entered a number that doesn't match the condition!")
