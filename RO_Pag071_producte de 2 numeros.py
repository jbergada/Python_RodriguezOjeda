#RO_Pag071_producte de 2 numeros.py

from math import *

print("n1 = ", end="")
n1 = int(input())

print("n2 = ", end="")
n2 = int(input())

resta1 = 1000-n1
resta2 = 1000-n2

suma = resta1+resta2
mil_suma = 1000 - suma
prod_mil = 1000 * mil_suma
prod_restes = resta1*resta2

resultat = prod_mil+prod_restes
print(resultat)

