# Предложите пользователю ввести имя человека, которого
# пользователь хочет пригласить на вечеринку. После этого выведите сообщение «[имя] has been invited» и увеличьте счетчик на 1. Спросите, хочет ли пользователь пригласить кого-то
# еще. Продолжайте запрашивать имена, пока пользователь не
# ответит отрицательно, и выведите количество приглашенных.

count = 0
name = input("Enter the name of the person you would like to invite: ")
print(f"{name} has been invited!")
count += 1
prompt = input("Would you like to invite someone else? (y/n) ").lower()
while prompt == "y":
    name = input("Enter the name of the person you would like to invite: ")
    print(f"{name} has been invited!")
    count += 1
    prompt = input("Would you like to invite someone else? (y/n) ").lower()
print(f"You've invited {count} person(s)!")
