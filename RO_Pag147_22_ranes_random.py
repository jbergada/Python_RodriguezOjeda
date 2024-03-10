import random
def salt():
    aleatori = random.randint(0,3)
    if (aleatori == 0):
        return 0
    elif (aleatori == 1):
        return 0.5
    elif (aleatori == 2):
        return -0.5
    else:
        return 1
pos_rana1 = 0
pos_rana2 = 0
pos_rana3 = 0
cont = 0
while (pos_rana1 < 20 and pos_rana2 < 20 and pos_rana3 < 20):
    pos_rana1 = pos_rana1 + salt()
    pos_rana2 = pos_rana2 + salt()
    pos_rana3 = pos_rana3 + salt()
    cont = cont + 1;
    print("Posició de la rana1: ", pos_rana1)
    print("Posició de la rana2: ", pos_rana2)
    print("Posició de la rana3: ", pos_rana3)
print(cont)
    