# Предложите пользователю ввести общую сумму счета, а затем запросите общее
# количество участников обеда. Разделите сумму счета на количество участников
# и выведите сумму, которую должен заплатить каждый участник.

bill = float(input("Please, enter the cost of the bill: "))
persons = int(input("Please, enter the number of persons: "))
costPerPerson = round(bill / persons, 2)
print("Cost per person: $",costPerPerson)
