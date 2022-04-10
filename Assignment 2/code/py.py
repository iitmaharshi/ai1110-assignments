import mpmath as mp
import numpy as np


a = float(input())
b = float(input())

c = float(mp.tan(mp.pi - mp.atan(a) - mp.atan(b)))

x = a + b + c
y = a*b*c
epsilon = 10**-4

if abs(x-y) < epsilon:
    print("verified and true")
else:
    print("false")
