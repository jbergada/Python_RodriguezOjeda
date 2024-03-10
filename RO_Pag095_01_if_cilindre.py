#RO_Pag091_1_if_cilindre.py

from math import *

radi = 20
altura = 30

if altura > radi:
    volum = pi * pow(radi,2)
    print("volum = ", volum)
else:
    area = 2 * pi * radi * (radi+altura)
    print("area =", area)
