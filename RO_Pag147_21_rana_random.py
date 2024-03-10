#RO_pag147_rana_random.py

import random

def salt():
    aleatori = random.randint(0,1)
    if (aleatori == 0):
        return -1
    else:
        return 1


pos_rana = 10
cont = 0

while (pos_rana > 0 and pos_rana < 20):
    pos_rana = pos_rana + salt()
    cont = cont + 1;
    print("Posición de la rana: ", pos_rana)
    
print("Numero de salts: ", cont)
print("Posició de la rana: ", pos_rana)

