# RO_Pag081_volum_cilindre.py

from math import *

print("Volum d'un cilindre")
print("radi en m: ",end="")
radi = float(input())
print("altura en m: ", end="")
altura = float(input())

volum = pi*pow(radi,2)*altura
print("volum = ", volum, "m3")
