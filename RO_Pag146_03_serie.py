#RO_Pag146_03_serie.py

from math import *

base = 1
exponent = 1

suma = pow(base,exponent)
i = 1
x = int(input("Introdueix el número a superar per la sèrie: "))

while suma < x:
    base = base + 1
    exponent = exponent + 1
    suma = suma + pow(base, exponent)
    i = i + 1

print("Han calgut ", i , " termes de la sèrie per superar el ", x)