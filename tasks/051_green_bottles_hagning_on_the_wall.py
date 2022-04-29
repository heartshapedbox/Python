# Выведите строки «There are [счетчик] green bottles hanging on the wall, [счетчик] green bottles
# hanging on the wall, and if 1 green bottle should accidentally fall». Затем выведите вопрос: «how many
# green bottles will be hanging on the wall?». Если пользователь ответит правильно, выведите сообщение «There will be [счетчик] green bottles hanging on the wall». Если пользователь ответит неправильно, выведите сообщение «No, try again», пока не будет дан правильный ответ. Когда счетчик уменьшится до 0, выведите сообщение «There are no more green bottles hanging on the wall».

count = 10
print(f"There are {count} green bottles hanging on the wall, {count} green bottles hanging on the wall, and if 1 green bottle should accidentally fall.")
while count != 0:
    count -= 1
    prompt = int(input("How many green bottes will be hanging on the wall? "))
    while prompt != count:
        print("No, try again!")
        prompt = int(input("How many green bottes will be hanging on the wall? "))
    print(f"There will be {count} green bottles hanging on the wall!")
    print(f"There are {count} green bottles hanging on the wall, {count} green bottles hanging on the wall, and if 1 green bottle should accidentally fall.")
print("There are no more green bottles hanging on the wall!")
