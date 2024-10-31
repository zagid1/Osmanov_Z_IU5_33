class Student:
    _a = list()
    _b = int
    def __init__(self, a_, b_):
        self.__a = a_
        self.__b = b_

a = Student(10, 12)
print()
print(f"Student: {a._Student__a} and {a._Student__b}" )