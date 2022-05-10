# Предложите пользователю ввести пароль, а затем
# предложите ввести его повторно. Если два пароля совпадут, выведите сообщение «Thank you». Если буквы
# введены правильно, но различаются регистром, выведите сообщение «They must be in the same case»;
# в противном случае выводится сообщение «Incorrect».

passcode = input("Please, enter a passcode: ")

confirmed = False
while confirmed == False:
    passcodeConfirm = input("Please, confirm your passcode: ")
    if len(passcode) != len(passcodeConfirm):
        print("Incorrect! Passcodes lengths do not match!")
        confirmed = False
    elif passcode != passcodeConfirm:
        passcodeList = [i for i in passcode]
        passcodeConfirmList = [i for i in passcodeConfirm]
        lowerPasscodeList = [i.lower() for i in passcode]
        lowerPasscodeConfirmList = [i.lower() for i in passcodeConfirm]
        caseFeedback = []
        if lowerPasscodeList == lowerPasscodeConfirmList:
            for i in range(0, len(passcodeList)):
                if passcodeList[i].islower() and passcodeConfirmList[i].isupper():
                    caseFeedback.append("Incorrect! Passcodes must be in the same case!")
                elif passcodeList[i].isupper() and passcodeConfirmList[i].islower():
                    caseFeedback.append("Incorrect! Passcodes must be in the same case!")
            print(caseFeedback[0])
            confirmed = False
        else:
            print("Incorrect! Passcodes do not match!")
            confirmed = False
    else:
        print("Correct! Thank you!")
        confirmed = True
