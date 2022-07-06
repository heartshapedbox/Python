import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
        
    @classmethod
    def diameter(cls, _diameter):
        return cls(radius = _diameter / 2)
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __repr__(self):
        return f'{self.__class__.__name__}(radius = {self.radius})'
        

circle = Circle.diameter(30)
for i in (circle, circle.area(), circle.perimeter()):
    print(i)