#RO_Pag071_area_triangle.py

from math import *

print("Introdueix el valor de la diagonal: ", end="")
d = float(input())

print("introdueix el valor de l'angle: ", end="")
alfa = float(input())

alfa = alfa * (pi/180) # pas a rad

a = d * sin(alfa)
b = d * cos(alfa)

area = (a * b)/2
print("Area del triangle = ", area)