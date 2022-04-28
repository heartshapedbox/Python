# Предложите пользователю ввести число больше 100, а затем число меньше 10. Сообщите, сколько раз меньшее число помещается в большем, в удобном формате.

maxNumber = int(input("Please, engter a number higher that 100: "))
minNumber = int(input("Please, engter a number lower that 10: "))
result = maxNumber // minNumber
leftover = maxNumber % minNumber
print(f"{maxNumber} consists {minNumber} - {result} times. Leftover - {leftover}")
