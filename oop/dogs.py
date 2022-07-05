class Dog:
    species = 'Canis familiaris'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} is {self.age} age old.'
        
    def speak(self, sound):
        return f'{self.name} says {sound} '


jeff = Dog('Jeff', 5)
# print(jeff.description(), jeff.speak('Woof Woof.'))


joy= Dog('Joy', 7)
# print(joy.description(), joy.speak('Woof Woof.'))


print(jeff)
print(joy)
