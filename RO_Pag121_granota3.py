# RO_Pag121_granota3.py

from random import*
x=0
y=0
i=0

while not((x == 4 and y == 4) or (x == -4 and y == 4) or (x == 4 and y == -4)or (x == -4 and y == -4)):  
    
    d=randint(1,4)
    i=i+1
    if d==1:
        x=x+1
    elif d==2:
        x=x-1
    elif d==3:
        y=y+1
    else:
        y=y-1
    
    if x == 5:
        x = x - 1
    elif x == -5:
        x = x + 1
    elif y == 5 :
        y = y - 1
    elif y == -5:
        y = y + 1
    print(x,y)
    print("Quantitat d'intents",i)
