from lab_python_oop.Color import figureColor
from lab_python_oop.rectangale import Rectangle
from colorama import init, Fore, Back, Style 

class Square(Rectangle):
    def __init__(self, side, color):
        self.name = "Квадрат"
        self.side = side
        self.squareColor = figureColor(color)

    def area(self):
        return self.side**2

    init()
    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            self.name,
            self.squareColor.color,
            self.side,
            self.area()
        )