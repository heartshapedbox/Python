# Напишите программу, которая предлагает ввести промежуток времени в днях,
# а потом выводит количество часов, минут и секунд в этом промежутке.

days = int(input("Please, enter the number of days: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("There are",hours,"hours,",minutes,"minutes,",seconds,"seconds in",days,"days.")
