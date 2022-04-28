# В одном килограмме 2,204 фунта. Предложите пользователю ввести вес в килограммах и переведите его в фунты.
kgWeight = int(input("Please, enter your weight (kg): "))
lbWeight = round(kgWeight * 2.204, 2)
print("Your weight in pounds is: ",lbWeight,"lb.")
