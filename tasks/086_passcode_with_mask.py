passcode = input("Please, enter a passcode: ")

confirmed = False
while confirmed == False:
    passcodeConfirm = input("Please, confirm your passcode: ")
    if len(passcode) != len(passcodeConfirm):
        print("[-] Incorrect! Passcodes lengths do not match!")
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
                    caseFeedback.append("[-] Incorrect! Passcodes must be in the same case!")
                elif passcodeList[i].isupper() and passcodeConfirmList[i].islower():
                    caseFeedback.append("[-] Incorrect! Passcodes must be in the same case!")
            print(caseFeedback[0])
            confirmed = False
        else:
            print("[-] Incorrect! Passcodes do not match!")
            confirmed = False
    else:
        mask = ""
        for i in range(1, len(passcode) - 1):
            mask += "*"

        sliced1 = slice(0, 1)
        sliced2 = slice(len(passcode) - 1, len(passcode))
        hiddenPass = passcode[sliced1] + mask + passcode[sliced2]

        print(f"[+] Correct! Thank you! Your passcode is {hiddenPass}")
        confirmed = True
