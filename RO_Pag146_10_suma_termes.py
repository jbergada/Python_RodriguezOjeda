# RO_Pag146_10_suma_termes.py

from math import *
n_max = 5
suma = 0
exponent = 3
terme = 0

n = 1
while n <= n_max:
    terme = pow(n, exponent)
    suma = suma + terme
    n = n + 1
print("La suma de la sèrie n3 + (n+1)3 + ... =", suma)
    
    