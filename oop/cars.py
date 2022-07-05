class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def release_date(self, month):
        return f"{self.brand} {self.model} {self.year} {self.color} will be released in {month}, {self.year}"

car1 = Car("RoadRunner", "Classic", 2049, "Glossy White")
print(car1.release_date("January"))

car2 = Car("RoadRunner", "4x4", 2049, "Matte Anthracite")
print(car2.release_date("August"))

class SportCar(Car):
    def __init__(self, model, base, year, color, convertible, turbo):
        super().__init__(model, base, year, color)
        self.convertible = convertible
        self.turbo = turbo

    def release_date(self, month):
        if self.convertible == True and self.turbo == True:
            self.convertible = "Convertible"
            self.turbo = "Turbo"
            return f"{self.brand} {self.turbo} {self.model} {self.year} {self.convertible} {self.color} will be released in {month}, {self.year}"
        elif self.convertible == True and self.turbo == False:
            self.convertible = "Convertible"
            return f"{self.brand} {self.model} {self.year} {self.convertible} {self.color} will be released in {month}, {self.year}"
        elif self.convertible == False and self.turbo == True:
            self.turbo = "Turbo"
            return f"{self.brand} {self.turbo} {self.model} {self.year} {self.color} will be released in {month}, {self.year}"
        return f"{self.brand} {self.model} {self.year} {self.color} will be released in {month}, {self.year}"

car3 = SportCar("RoadRunner", "Sport", 2049, "Glossy Red", False, False)
print(car3.release_date("June"))

car4 = SportCar("RoadRunner", "Sport", 2049, "Glossy Lime", False, True)
print(car4.release_date("August"))

car5 = SportCar("RoadRunner", "Sport", 2049, "Glossy Lime", True, True)
print(car5.release_date("September"))
