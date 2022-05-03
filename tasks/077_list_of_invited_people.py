# Предложите пользователю ввести имена трех людей, которых он хочет
# пригласить на вечеринку, и сохраните их в списке. После того как будут
# введены все три имени, спросите, хочет ли пользователь добавить еще
# одно имя. Если ответ будет положительным, предложите ему добавлять
# имена, пока не получите ответ «no». После ответа «no» выведите полный список имен. Предложите пользователю ввести одно из имен в списке и выведите позицию имени в списке. Спросите, хочет ли пользователь, чтобы этот человек присутствовал на вечеринке. Если пользователь ответит «no», удалите элемент из списка и снова выведите список.

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
print(names)
nameFromList = names.index(input("Enter some name from the list above: "))
prompt = input("Would like to see this person on the party? (y/n) ").lower()
if prompt == "n":
    del names[nameFromList]
    print("Done!",names)
else:
    print("Done!",names)
