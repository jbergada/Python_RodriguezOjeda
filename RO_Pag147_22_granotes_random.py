# RO_Pag147_22_granotes_random

from random import *
pos_granota_1 = 0
pos_granota_2 = 0
pos_granota_3 = 0
salts = 0
while ((pos_granota_1 < 20) and (pos_granota_2 < 20) and (pos_granota_3 < 20)):
    
    salt_granota_1 = randint(0,3)
    if salt_granota_1 == 0:
        pos_granota_1 = pos_granota_1 + 0.5
    elif salt_granota_1 == 1:
        pos_granota_1 = pos_granota_1 + 1
    elif salt_granota_1 == 2:
        pos_granota_1 = pos_granota_1 - 0.5
    elif salt_granota_1 == 3:
        pos_granota_1 = pos_granota_1 + 0
        
    salt_granota_2 = randint(0,3)
    if salt_granota_2 == 0:
        pos_granota_2 = pos_granota_2 + 0.5
    elif salt_granota_2 == 1:
        pos_granota_2 = pos_granota_2 + 1
    elif salt_granota_2 == 2:
        pos_granota_2 = pos_granota_2 - 0.5
    elif salt_granota_2 == 3:
        pos_granota_2 = pos_granota_2 + 0
    
    salt_granota_3 = randint(0,3)
    if salt_granota_3 == 0:
        pos_granota_3 = pos_granota_3 + 0.5
    elif salt_granota_3 == 1:
        pos_granota_3 = pos_granota_3 + 1
    elif salt_granota_3 == 2:
        pos_granota_3 = pos_granota_3 - 0.5
    elif salt_granota_3 == 3:
        pos_granota_3 = pos_granota_3 + 0
    
    salts = salts + 1
    print("salt ", salts)
    print("posició de la granota 1 = ",pos_granota_1)
    print("posició de la granota 2 = ", pos_granota_2)
    print("posició de la granota 3 = ", pos_granota_3)
    
    if pos_granota_1 >= 20:
        print("Ha guanyat la granota 1")
    elif pos_granota_2 >= 20:
        print("Ha guanyat la granota 2")
    elif pos_granota_3 >= 20:
        print("Ha guanyat la granota 3")