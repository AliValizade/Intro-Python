import math
from unittest import result
# حل معادله درجه 2
# a * x**2 + b * x + c = 0
a = int(input())
b = int(input())
c = int(input())
if a==0:
    print("a Can't be zero")
    exit()
    
Δ = b**2 - 4*a*c

if Δ < 0:
    print("No Answer😎")

elif Δ > 0:
    x1 = (-b - math.sqrt(Δ)) / (2*a)
    x2 = (-b + math.sqrt(Δ)) / (2*a)
    print(x1)
    print(x2)

elif Δ == 0:
    x = -b / (2 * a)
    print(x)
