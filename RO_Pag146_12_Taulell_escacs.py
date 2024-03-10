# RO_Pag146_12_Taulell_escacs.py
from math import *

suma = 0

i = 1
exponent = 64
while i < exponent:
    suma = pow(2,i) + suma
    print(pow(2,i), " ", suma)
    i = i + 1
print("Calen ", suma/20000000, "tones de blat")

    
