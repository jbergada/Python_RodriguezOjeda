#RO_Pag148_23_boles_bossa.py
from random import *
#bossa_boles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = True
while a == True:
    bola = randint(1,10)
    if bola < 1 or bola > 10:
        a == False
    else:
        print("bola extreta = ", bola)