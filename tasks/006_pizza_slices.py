# Спросите, сколько кусков пиццы
# было у пользователя и сколько
# кусков он съел. Вычислите, сколько кусков пиццы у него осталось,
# и выведите результат в форме,
# удобной для пользователя.

pizzaSlices = int(input("How many slices of pizza did you have?: "))
eatenPizzaSlices = int(input("How many slices of pizza have you eaten?: "))
result = pizzaSlices - eatenPizzaSlices
print("You still have",result,"slice(s) of pizza.")
