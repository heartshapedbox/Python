# Предложите пользователю
# ввести первую строку какогонибудь стихотворения, выведите длину строки. Запросите
# начальную и конечную позицию и выведите только эту
# часть строки (не забудьте, что
# в Python нумерация индексов
# начинается с 0, а не с 1).

textLine = input("Enter a line of some text: ")
print(len(textLine))
startPosition = int(input("Enter the start number: "))
endPosition = int(input("Enter the end number: "))
print(textLine[startPosition:endPosition])
