import numpy as np
from numpy import random as RN

N = 36

n_0 = 25
n_1 = 11

pr_0 = n_0/N
pr_1 = n_1/N

x = RN.randint(1,101,size = N)

x_0 = np.count_nonzero(x>31)
x_1 = N - x_0

Pr_0 = x_0/N
Pr_1 = x_1/N

print("Theoritical probabilities: ",pr_0, pr_1)
print("Practical probabilities: ",Pr_0,Pr_1)