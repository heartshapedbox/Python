# Предложите пользователю
# ввести его почтовый индекс.
# Выведите первые две буквы
# слова в верхнем регистре
# .

index = input("Please, enter your post index code: ")
for i in range(0, 2):
    print(index[i].upper(), end = "")
