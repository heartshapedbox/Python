

class Dog:
    species = 'Canis familiaris'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} is {self.age} age old.'
        
    def speak(self, sound):
        return f'{self.name} says {sound} '


dog_jeff = Dog('Jeff', 5)
# print(dog_jeff.description(), dog_jeff.speak('Woof Woof.'))


dog_joy= Dog('Joy', 7)
# print(dog_joy.description(), dog_joy.speak('Woof Woof.'))


print(dog_jeff)
print(dog_joy)
