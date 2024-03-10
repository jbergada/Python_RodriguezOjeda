# RO_Pag147_17_aleatori_primer.py

from random import *
numero = randint(1,100)
numero_original = numero
while numero < 3:
    residu = numero%(numero-1)
    if residu != 0:
        numero = numero-1
    if numero == 3 and residu != 0:
        print("El número ", numero_original, " és primer ")
    else:
        print("El número ", numero_original, " no és primer")

    
