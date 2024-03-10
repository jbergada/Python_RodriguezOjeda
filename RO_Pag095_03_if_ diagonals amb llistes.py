# RO_Pag095_03_if_ diagonals amb llistes.py
from math import *

x = float(input("Introdueix l'altura x = "))
y = float(input("Introdueix l'altura y = "))
z = float(input("Introdueix l'altura z = "))

diagonal1 = sqrt(pow(x,2) + pow(y,2))
diagonal2 = sqrt(pow(x,2) + pow(z,2))
diagonal3 = sqrt(pow(y,2) + pow(z,2))

llista = [diagonal1, diagonal2, diagonal3]

if llista[0]==llista[1]==llista[2]:
    print("Les diagonals son iguals i de valor", diagonal1)
elif llista[0] == llista[1]:
    if llista[0] > llista[2]:
        print("Les més grans són diagonal1 = diagonal2 = ",diagonal1)
    else:
        print("La diagonal més gran és diagonal3= ",diagonal3)

elif llista[0] == llista[2]:
    if llista[0] > llista[1]:
        print("Les més grans són diagonal1 = diagonal3 =", diagonal1)
    else:
        print("La més gran és diagonal2= ",diagonal2)

elif llista[1] == llista[2]:
    if llista[1] > llista[0]:
        print("Les més grans són diagonal2 = diagonal3 =", diagonal2)
    else:
        print("La més gran és diagonal1= ", diagonal1)

elif llista[0] > llista[1] and llista[0] > llista[2]:
    print("La més gran és diagonal1 = ", diagonal1)
elif llista[1] > llista[2] and llista[1] > llista[0]:
    print("La més gran és diagonal2 = ", diagonal2)
else: 
    print("La més gran és diagonal3 = ", diagonal3)
