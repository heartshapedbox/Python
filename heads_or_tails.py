import math
import random
arrayCoin = ["Head","Tail"]
invitation = input("Hello!\nWould you like to play 'Heads or Tails' game?\nI will toss a coin and you will guess. (y/n) ")

while invitation == "y":
    guess = input("OK, let's go!\nHead is 'h', and Tail is 't'. What is your choice? ")
    coin = random.choice(arrayCoin)
    if coin == "Head" and guess == "h":
        print("Hey! Look at this! It's a",coin,"! You win!")
    elif coin == "Tail" and guess == "t":
        print("Hey! It's a",coin,"! Look at you! You win!")
    elif coin == "Head" and guess == "t":
        print("Meh! You lose! It was a",coin,".")
    elif coin == "Tail" and guess == "h":
        print("Meh! You lose! It was a",coin,".")
    else:
        print("Sorry! I don't understand.")
    invitation = input("Would you like to try again? ")
print("OK! I won't bother you!")
