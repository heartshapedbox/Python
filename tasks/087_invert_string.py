# Предложите пользователю ввести слово, а затем
# выведите буквы слова в обратном порядке в разных
# строках. Например, если пользователь ввел строку
# «Hello», результат должен выглядеть так:
# Enter a word: Hello
# o
# l
# l
# e
# H
# >>>

prompt = input("Please, enter some word: ")
for i in range(len(prompt) - 1, -1, -1):
    print(prompt[i])
