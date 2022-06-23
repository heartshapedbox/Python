parentsList = ['Distance: Kilometer > Meter','Distance: Kilometer > Mile','Weight: Kilo > Gram','Weight: Kilo > Pound']
parentsDict = {}
for i in range(0, len(parentsList)):
    parentsDict[i + 1] = parentsList[i]
    
print(parentsDict)