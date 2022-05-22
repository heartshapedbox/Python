shows = ["SNL","Conan","Talking Dead","Tonight Show"]
showsDict = {}
for i in shows:
    showsDict[shows.index(i)] = i
print(showsDict)

prompt = input("\nPlease, enter another show and its position in the list using ',': ")
anotherShow = prompt.split(",")[0]
anotherShowIndex = prompt.split(",")[1]

shows = []
for i in showsDict:
    shows.append(showsDict[i])
shows.insert(int(anotherShowIndex), anotherShow)

for i in shows:
    showsDict[shows.index(i)] = i
print(showsDict)
