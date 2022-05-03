# Предложите пользователю ввести имена трех людей, которых он хочет
# пригласить на вечеринку, и сохраните их в списке. После того как будут
# введены все три имени, спросите, хочет ли пользователь добавить еще
# одно имя. Если ответ будет положительным, предложите ему добавлять
# имена, пока не получите ответ «no». После ответа «no» выведите количество людей, приглашенных на вечеринку

name = input("Please, enter a name of person you would like to invite: ")
names = [name]
for i in range(0, 2):
    name = input("Please, enter another name of person you would like to invite: ")
    names.append(name)
prompt = input("Would you like to invite one more? (y/n) ").lower()
while prompt == "y":
    name = input("Enter a name of person you would like to invite: ")
    names.append(name)
    prompt = input("Would you like to invite one more? (y/n) ").lower()
print(f"Your've invited {len(names)} people!")
