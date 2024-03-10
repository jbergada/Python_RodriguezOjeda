#RO_Pag081_7_poblacio.py
from math import *


t = 5
n = (5 * t) + (2 * exp(0.1*t))
print("n(5)= ",n)

t = 10
n = (5 * t) + (2 * exp(0.1*t))
print("n(10)= ",n)

t = 20
n = (5 * t) + (2 * exp(0.1*t))
print("n(20)= ",n)

t = [5, 10, 20]

for i in t:
    n = (5 * i) + (2 * exp(0.1*i))
    print("n",[i], " = ",n)

for i in range(0,3):
    n = (5 * t[i]) + (2 * exp(0.1*t[i]))
    print("n[",t[i],"] = ",n)
    