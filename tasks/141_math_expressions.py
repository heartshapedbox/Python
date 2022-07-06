numberQuantity = int(input("Hello! This is The HappyNumbers.\nHow many numbers would you like to use? -- "))
method = input("\nWhat would you like to do with the numbers?\nChoose an operation:\na) Addition\nb) Subtraction\nc) Multiplication\nd) Division\n\nYour choise is -- ")

print("\n")

maxLength = int(numberQuantity)
array = []
while len(array) < maxLength:
    num = input("Please, enter a number: ")
    array.append(int(num))

def sum():
    result = 0
    for i in array:
        result += i
    return result
def mult():
    result = 1
    for i in array:
        result *= i
    return result
def sub():
    result = 0
    start = array[0]

    for i in range(1, len(array)):
        result = start - array[i]
        start = result
    return result
def div():
    result = 0
    start = array[0]

    for i in range(1, len(array)):
        result = round(start / array[i], 2)
        start = result
    return result

if method == "a":
    print("\nThe result is: ", sum())
elif method == "b":
    print("\nThe result is: ", sub())
elif method == "c":
    print("\nThe result is: ", mult())
else:
    print("\nThe result is: ", div())
