#RO_Pag071_beneficis.py

from math import *

print("Número d'articles = ",end="")
n = int(input())

despeses = 50 + 2*n 
ingressos = 2.4*n
benefici = ingressos-despeses

print("Benefici = ", benefici, " €")

n = ceil(50/1.4)
print(n)
