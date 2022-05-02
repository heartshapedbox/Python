# Выведите названия пяти цветов, случайным образом выберите один и предложите сделать то же пользователю. Если пользователь выберет тот же
# цвет, который выбрала программа, выведите сообщение «Well done»; в противном случае выведите ответ, в котором скрывается намек на правильный
# цвет. Предложите пользователю повторить попытку; если пользователь и на
# этот раз не угадает, снова выведите ту же подсказку и предложите выбрать
# цвет (и так далее, пока пользователь не выдаст правильный ответ).

import random
def checkList():
            match = 0
            for i in colors:
                global guess
                if guess == i:
                    match += 1
                else:
                    match += 0
            return match
def guessRandomColor():
            result = checkList()
            if result == 0:
                print("Error!")
            else:
                global guess
                if guess == randomColor:
                    print("\nWell done! You guessed it right!")
                else:
                    hint = input("\nYou guessed it wrong! Need a small hint? (y/n) ").lower()
                    if hint == "y":
                        if randomColor == "Black":
                            hintText = "It seems that I saw that colour on Zebra's body."
                        elif randomColor == "Blue":
                            hintText = "It could be a color of the sky or a feeling of sadness."
                        elif randomColor == "Brown":
                            hintText = "I'm pretty sure it sounds very familiar with 'Mr'."
                        elif randomColor == "Yellow":
                            hintText = "It's between green and orange on the spectrum of visible light."
                        else:
                            hintText = "It's somehow related to carpet."
                        print(hintText)
                        guess = input("Go on! Try again!: ").title()
                        if guess == randomColor:
                            print("\nWell done! Second try and you got it!")
                        else:
                            print("\nYou guessed it wrong again! Let's try next time.")
                    elif hint == "n":
                        guess = input("OK. No hint! Try again!: ").title()
                        if guess == randomColor:
                            print("\nWell done! Second try and you got it!")
                        else:
                            print("\nYou guessed it wrong again! Let's try next time.")
                    else:
                        print("Error!")

invitation = input("Hey! Would you like to play 'Guess a Color?' (y/n) ").lower()

if invitation == "y":
    colors = ["Black","Blue","Brown","Yellow","Red"]
    randomColor = random.choice(colors)
    print("\n",colors)
    print("Look at these colors above. I've picked one. Guess which one.")
    guess = input("You have 2 attemps. Try: ").title()
    checkList()
    guessRandomColor()
elif invitation == "n":
    print("Got it! I won't bother you!")
else:
    print("Error!")
