import sys
import math

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
        return get_coeff(prompt)
    

def solve_quad(a, b, c):
    dis = b**2 - 4 * a * c
    if dis > 0:
        temp1 = (-b + dis**0.5) / (2 * a)
        temp2 = (-b - dis**0.5) / (2 * a)
        return temp1, temp2
    elif dis == 0:
        temp = -b / (2 * a)
        return temp, None
    else:
        return None, None

def solve_biq(a, b, c):
    if a == 0:
        print("A = 0.")
        return
    temp1, temp2 = solve_quad(a, b, c)
    roots = []
    if temp1 is not None and temp1 >= 0:
        x1 = temp1**0.5
        x2 = - temp1**0.5
        roots += [x1, x2]

    if temp2 is not None and temp2 >= 0:
        x3 = temp2**0.5
        x4 = - temp2**0.5
        roots += [x3, x4]
    print(roots)
    if len(roots):
        print("корни уравнения: ", sorted(set(roots)))
    else:
        print("корней нет.")


a = get_coeff_sys(1, "Коэффициент A: ")
b = get_coeff_sys(2, "Коэффициент B: ")
c = get_coeff_sys(3, "Коэффициент C: ")

solve_biq(a, b, c)

