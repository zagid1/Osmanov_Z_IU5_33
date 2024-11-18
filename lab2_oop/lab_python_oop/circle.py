from lab_python_oop.geometric_shape import geometricShape
from lab_python_oop.Color import figureColor
import math
from colorama import init, Fore, Back, Style 

class Circle (geometricShape):
    def __init__(self, radius, color):
        self.name = "Круг"
        self.radius = radius
        self.circleColor = figureColor(color)
    
    def area(self):
        return math.pi * self.radius**2
    
    init()
       
    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            self.name,
            self.circleColor.color,
            self.radius,
            self.area()
        )