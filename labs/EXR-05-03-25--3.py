#module 
import math

# dir(math)
# print(help(math.sqrt))
# print(dir(math))

def get_root(number):
    return math.sqrt(number)
square = get_root(4)
print(f"The root - {square}")

def add_numbers(a,b):
    sum = a + b
    return get_root(sum)
result = add_numbers(7, 2)
print(f"The root - {result}")
