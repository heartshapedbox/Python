class Dog():
    species = 'Canis familiaris'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'{self.name} is {self.age} age old.'
    
    def speak(self, sound):
        return f'{self.name} says {sound}.'
        

jeff = Dog('Jeff', 5)
jack = Dog('Jack', 7)

for i in (jeff, jeff.speak('Whoof'), jack, jack.speak('Ahw')):
    print(i)
    
   

class GoldenRetriever(Dog):
    def speak(self, sound = 'Bark'):
        return super().speak(sound)


jim = GoldenRetriever('Jim', 9)

for i in (jim, jim.speak()):
    print(i)