class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def __str__(self):
        return f'The {self.color} car has {self.mileage} miles.'

blue_car = Car("Blue", "20,000")
red_car = Car("Red", "30,000")

for i in (blue_car, red_car):
    print(i)