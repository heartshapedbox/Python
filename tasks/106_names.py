# Создайте новый файл с именем Names.txt. Добавьте в него пять имен,
# отображающихся на разных строках. После запуска программы найдите
# папку, в которой располагается ваша программа; убедитесь в том, что файл
# был создан.

import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

file = open("Names.txt", "w")
file.write("Jack\n")
file.write("John\n")
file.write("Anna\n")
file.write("Mike\n")
file.write("Jane")
file.close()
