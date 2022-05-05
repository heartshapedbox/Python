# Выведите строку из своего любимого стихотворения и предложите
# пользователю ввести начальную и конечную позицию. Выведите
# символы, находящиеся между ними.

poem = "Deep into that darkness dusking, I heard a gala, dark bedding"
print(poem)

start = int(input("\nPlease, enter a number for start position: "))
finish = int(input("\nPlease, enter another number for finish position: "))

print(poem[start:finish])
