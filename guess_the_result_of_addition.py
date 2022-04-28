import random

print("Guess the result of addition of 2 random numbers from 1 to 5.\nYou have 5 attempts and for each correct one you'll get 1 point.")

count = 0
score = 0

while count < 5:
    num1, num2 = random.randint(1, 5), random.randint(1, 5)
    sum = num1 + num2
    guess = int(input("Try! Enter the resut: "))
    if sum == guess:
        print("You guessed it right! The result is:",num1,"+",num2,"=",sum,". You get 1 point!")
        score += 1
    else:
        print("You guessed it wrong! The result is:",num1,"+",num2,"=",sum,".")
    count += 1
print("\nYou guessed the result",score,"time(s). You get",score,"point(s).")
