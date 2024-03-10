#RO_Pag146_granota00.py

import random

# for i in range(1,20):
#     print(salt())

pos_rana = 10
cont = 0

while (pos_rana > 0 and pos_rana < 20):
    aleatori = random.randint(0,1)
    if aleatori == 0:
        salt = -1
    else:
        salt = 1
        
    pos_rana = pos_rana + salt
    cont = cont + 1;
    print("Posició de la granota: ", pos_rana)
    
print("Numero de salts: ", cont)
print("Posició de la granota: ", pos_rana)

