# Предложите пользователю ввести слово в верхнем регистре. Если
# не все буквы слова будут указаны в верхнем регистре, попросите
# ввести слово заново. Повторяйте попытки, пока пользователь не
# введет сообщение в верхнем регистре.

word = input("Please, enter some word in uppercase: ")
while word != word.upper():
        word = input("It's not in uppercase. Please, enter a word in uppercase: ")
print(word)
