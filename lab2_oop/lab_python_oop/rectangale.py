from lab_python_oop.geometric_shape import geometricShape
from lab_python_oop.Color import figureColor
from colorama import init, Fore, Back, Style 

class Rectangle(geometricShape):
    def __init__(self, height, width, color):
        self.name = "Прямоугольник"
        self.width = width
        self.height = height
        self.rectangleColor = figureColor(color)
    
    def area(self):
        return self.width * self.height
    
    init()
    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            self.name,
            self.rectangleColor.color,
            self.width,
            self.height,
            self.area()
        )