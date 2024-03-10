# RO_Pag146_09_coordenades.py
from math import *
suma = 0
n = 1
n_max = 4
while n <= n_max:
    print("x",n ,"= ", end="")
    x = float(input())
    print("y",n , "= ",end="")
    y = float(input())
    d = sqrt(pow(x,2) + pow(y,2))
    suma = suma + d
    n = n + 1
print(suma)
    