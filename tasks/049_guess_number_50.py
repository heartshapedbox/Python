# Создайте переменную с именем compnum и присвойте ей
# значение 50. Предложите пользователю ввести число. Пока
# предположение не совпадает
# со значением compnum, сообщите, больше оно или меньше
# compnum, и предложите ввести
# другое число. Если введенное
# значение совпадет с compnum,
# выведите сообщение «Well done,
# you took [попытки] attempts».

compnum = 50
count = 1
num = int(input("Please, enter a number: "))
while num != compnum:
    if num > compnum:
        print("Your number is higher!")
        num = int(input("Please, enter another number: "))
    else:
        print("Your number is lower!")
        num = int(input("Please, enter another number: "))
    count += 1
print(f"Well done, you took {count} attemp(s)!")
