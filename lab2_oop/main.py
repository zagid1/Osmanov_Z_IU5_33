from lab_python_oop.rectangale import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import init, Fore, Back, Style
def main():
    c = Circle(15, "Green")
    r = Rectangle(15, 15, "BLUE")
    s = Square(15, "RED")
    print(Fore.BLUE)
    print(r)
    print(Fore.GREEN)
    print(c)
    print(Fore.RED)
    print(s)
    print(Style.RESET_ALL)

if __name__ == "__main__":
    main()
