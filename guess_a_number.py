import math
import random
randomNumber = random.randrange(1,6)
guess = int(input("Hello! Pick a number from 1 to 5: "))

if guess == randomNumber:
    print("Well done! It's number",randomNumber)
elif guess > randomNumber:
    print("Your number is higher!")
    guess = int(input("Second try! Pick a number from 1 to 5: "))
    if guess == randomNumber:
        print("Correct! It's number",randomNumber)
    else:
        print("You lose! Correct number is",randomNumber)
else:
    print("Your number is lower!")
    guess = int(input("Second try! Pick a number from 1 to 5: "))
    if guess == randomNumber:
        print("Correct! It's number",randomNumber)
    else:
        print("You lose! Correct number is",randomNumber)
