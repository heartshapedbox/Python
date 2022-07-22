import getpass

account_number = getpass.getpass("Hello! Please, enter your card number: ")
account_number_to_array = [int(i) for i in account_number]


def f_check_card_number_length():
    if len(account_number_to_array) > 12:
        print("The card number length is incorrect! Please, launch a console again and enter a correct lengh of card number!")
        quit()
f_check_card_number_length()


def f_hide_numbers():
    for x in range(len(account_number_to_array)):
        if account_number_to_array.index(account_number_to_array[x]) < len(account_number_to_array) - 4:
            account_number_to_array[x] = "*"
f_hide_numbers()


array_to_string = "".join(str(e) for e in account_number_to_array)
print("The last 4 numbers of your card are: " + array_to_string)

confirm_card_number = input("Please, confirm your card number: Y/N ? ")

def f_confirm_card_number():
    if confirm_card_number == "Y":
        print("Your card is accepted!")
    else:
        print("The card is declined! Please, launch a console again and enter a correct card number!")
f_confirm_card_number()
