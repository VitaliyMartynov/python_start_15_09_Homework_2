from math import sqrt
a = int(input('enter length'))
b = int(input('enter length'))
c = int(input('enter length'))
p = (a + b + c) / 2
square = sqrt(p * (p - a) * (p -b) * (p - c))
print(square)