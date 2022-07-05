class Dog:
    species = 'Canis familiaris'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} is {self.age} age old.'
    
    def speak(self, sound):
        return f'{self.name} barks {sound}.'



class JackRussellTerrier(Dog):
    def speak(self, sound = 'Yap'):
        return f'{self.name} says {sound}.'


class Bulldog(Dog):
    def speak(self, sound = 'Woof'):
        return super().speak(sound)


jeff = JackRussellTerrier('Jeff', 10)
joy = Bulldog('Joy', 6)

for i in (jeff, jeff.speak(), joy, joy.speak()):
    print(i)


