#RO_Pag102_ramdom_while.py
# simulador fins que surti el número 6
from random import *
x = 0
comptador = 1
while x != 6:
    x = randint(1,6)
    print(comptador,  x)
    comptador = comptador + 1