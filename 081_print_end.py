# Предложите пользователю ввести его любимый школьный предмет.
# Выведите его так, чтобы после каждой буквы следовал дефис —
# например, S-p-a-n-i-s-h-.

prompt = input("Please, enter your favourite school subject: ")
for i in prompt:
    print(i, end = "-")
