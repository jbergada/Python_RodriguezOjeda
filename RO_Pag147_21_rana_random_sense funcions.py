#RO_Pag147_21_granota_random_sense funcions.py
from random import *
pos_granota = 10
comptador = 0

while (pos_granota > 0 and pos_granota < 20):
    salt = randint(0,1)
    if salt == 0:
        pos_granota = pos_granota - 1
    elif salt == 1:
        pos_granota = pos_granota + 1
    comptador = comptador + 1
    print("número de salts = ", comptador)
    print("posició de la granota = ", pos_granota)
    
print("posició de la granota = ", pos_granota)
print("número de salts = ", comptador)