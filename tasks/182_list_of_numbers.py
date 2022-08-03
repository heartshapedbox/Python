
numbersList = [int(input("Please, enter a nubmer: "))]
while len(numbersList) < 5:
    number = int(input("Please, enter another nubmer: "))
    numbersList.append(number)
    print(f"List of numbers: {numbersList}")
    if len(numbersList) > 3:
        prompt = input("Would you like to keep the last number? (y/n) ").lower()
        if prompt == "n":
            numbersList.remove(number)
            print(f"List of numbers: {numbersList}")
print(f"The result is: {numbersList}")
