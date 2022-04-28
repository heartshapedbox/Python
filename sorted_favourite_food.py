foodList = input("What is your favourite food? Use ',' to list it: ").title().split(",")
foodDict = {}
for i in foodList:
    foodDict[foodList.index(i) + 1] = i
print(foodDict)

removeFood = int(input("Enter the index of food you would like to remove: "))
del foodDict[removeFood]
print(sorted(foodDict.values()))
