# Спросите у пользователя, скольких людей он хочет пригласить на вечеринку. Если будет введено
# число меньше 10, запросите имена и после каждого имени выведите строку «[имя] has been invited».
# Если введенное число больше или равно 10, выведите сообщение «Too many people».

people = int(input("How many people would you like to invite?: "))
if people < 10:
    for i in range(0, people):
        name = input("Enter a name of person: ")
        print(f"{name} has been invited!")
else:
    print("Too many people!")
