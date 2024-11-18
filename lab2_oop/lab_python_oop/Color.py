class figureColor:
    def __init__(self, color):
        self.__color = color
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value
