# RO_Pag095_03_if_ diagonals amb llistes facil.py

from math import *
#llista = []
x = float(input("Introdueix l'altura x = "))
y = float(input("Introdueix l'altura y = "))
z = float(input("Introdueix l'altura z = "))

diagonal1 = sqrt(pow(x,2) + pow(y,2))
diagonal2 = sqrt(pow(x,2) + pow(z,2))
diagonal3 = sqrt(pow(y,2) + pow(z,2))

llista_noms = ["diagonal1 ", "diagonal2 ", "diagonal3 "]
print(llista_noms)
llista = [diagonal1, diagonal2, diagonal3]
print(llista)

llista.sort()
print(llista)
print("El valor de la diagonal més gran és ", llista[-1])