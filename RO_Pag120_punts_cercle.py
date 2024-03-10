#RO_Pag120_punts_cercle.py
#Punts aleatoris dins d'un cercle

from random import*
n=int(input('Quantitat d_intents: '))
c=0
for i in range(n):
    x=random()
    y=random()
    if x**2 + y**2 <= 1:
        c=c+1
print('Dentro del círculo: ',c)
