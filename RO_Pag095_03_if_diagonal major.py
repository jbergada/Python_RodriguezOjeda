#RO_Pag095_03_if_diagonal major.py
from math import *

x = float(input("Introdueix l'altura x = "))
y = float(input("Introdueix l'altura y = "))
z = float(input("Introdueix l'altura z = "))
"""
diagonal1 = (x**2 + y**2)**0.5
diagonal2 = (x**2 + z**2)**0.5
diagonal3 = (y**2 + z**2)**0.5

"""
diagonal1 = sqrt(pow(x,2) + pow(y,2))
diagonal2 = sqrt(pow(x,2) + pow(z,2))
diagonal3 = sqrt(pow(y,2) + pow(z,2))

if diagonal1 == diagonal2 and diagonal2 == diagonal3 :
    print("totes les diagonals són iguals i de valor", diagonal1)
elif diagonal1 == diagonal2:
    if diagonal1 > diagonal3:
        print("Les més grans són diagonal1 = diagonal2 = ",diagonal1)
    else:
        print("La diagonal més gran és diagonal3= ",diagonal3)
        
elif diagonal1 == diagonal3:
    if diagonal1 > diagonal2:
        print("Les més grans són diagonal1 = diagonal3 =", diagonal1)
    else:
        print("La més gran és diagonal2= ",diagonal2)
        
elif diagonal2 == diagonal3:
    if diagonal2 > diagonal1:
        print("Les més grans són diagonal2 = diagonal3 =", diagonal2)
    else:
        print("La més gran és diagonal1= ", diagonal1)
        
elif diagonal1 > diagonal2 and diagonal1 > diagonal3:
    print("La més gran és diagonal1 = ", diagonal1)
elif diagonal2 > diagonal3 and diagonal2 > diagonal1:
    print("La més gran és diagonal2 = ", diagonal2)
else: 
    print("La més gran és diagonal3 = ", diagonal3)
