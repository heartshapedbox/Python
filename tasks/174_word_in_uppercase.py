word = input("Please, enter some word in uppercase: ")
correct = False

while correct == False:
    if word.isupper():
        print(f"[+] Correct, {word} is in uppercase!")
        correct = True
    else:
        word = input(f"[-] No, {word} is not in uppercase! Please, enter a word in uppercase: ")
        correct = False
