#RO_Pag081_2_diametre_cilindre.py

from math import *

volum = float(input("volum del cilindre en litres: "))
altura = float(input("altura en metres: "))

volum = volum/1000
print("volum en m3: ", volum)

radi = sqrt(volum/(pi*altura))
diametre = 2 * radi

print("diàmetre del cilindre = ",diametre)

