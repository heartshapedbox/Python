# Предложите пользователю ввести любимый цвет. Если он введет «red», «RED»
# или «Red», выведите сообщение «I like red too». В противном случае выведите сообщение «I don’t like [colour], I prefer red».
color = input("Please, enter a color: ").lower()
if color == "red":
    print("I like red too!")
else:
    print(f"I don’t like {color}, I prefer red!")
