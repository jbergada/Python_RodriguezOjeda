#RO_Pag071_creixement poblacional.py

from math import *

k = (50 - (2*exp(0.1*10)))/10
print(k)

print("Temps en anys = ",end="")
t = float(input())

f_t= k * t + 2*exp(0.1*t)
print("f(t) = ",f_t)