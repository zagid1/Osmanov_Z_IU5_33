import sys
import math

class Biquadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve_quad(self):
        dis = self.b**2 - 4 * self.a * self.c
        
        if dis > 0:
            temp1 = (-self.b + dis**0.5) / (2 * self.a)
            temp2 = (-self.b - dis**0.5) / (2 * self.a)
            return temp1, temp2
        elif dis == 0:
            t = -self.b / (2 * self.a)
            return t, None
        else:
            return None, None 

    def solve_biq(self):
        if self.a == 0:
            print("A = 0.")
            return

        temp1, temp2 = self.solve_quad()

        roots = []
        if temp1 is not None and temp1 >= 0:
            x1 = temp1**0.5
            x2 = - temp1**0.5
            roots += [x1, x2]

        if temp2 is not None and temp2 >= 0:
            x3 = temp2**0.5
            x4 = - temp2**0.5
            roots += [x3, x4]

        if roots:
            print("корни уравнения: ", sorted(set(roots)))
        else:
            print("корней нет.")

class Input:

    def get_coeff(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Некорректный ввод.")

    def get_coeff_sys(arg_index, prompt):
        try:
            return float(sys.argv[arg_index])
        except (IndexError, ValueError):
            return Input.get_coeff(prompt)

a = Input.get_coeff_sys(1, "коэффициент A: ")
b = Input.get_coeff_sys(2, "коэффициент B: ")
c = Input.get_coeff_sys(3, "коэффициент C: ")

equation = Biquadratic(a, b, c)

equation.solve_biq()
