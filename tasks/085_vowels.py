# Предложите пользователю ввести имя,
# а затем сообщите, сколько в нем гласных букв.

name = input("Please, enter your name: ").lower()
vowels = ["a","e","i","o","u"];

count = 0
for i in name:
    if i in vowels:
        count += 1
    else:
        count += 0

if count > 1:
    print(f"There are {count} vowels in your name!")
else:
    print(f"There is {count} vowel in your name!")
