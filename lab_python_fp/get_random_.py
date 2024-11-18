from random import *

def get_random(amount, start, end):
    for i in range(amount):
        yield randint(start, end)

for item in get_random(5, 10, 100):
    print(item)