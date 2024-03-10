#RO_Pag095_11_if_distancies.py
from math import *

x1=4
y1=4
x2=4
y2=4

p1= sqrt(pow(x1,2)+pow(y1,2))
p2= sqrt(pow(x2,2)+pow(y2,2))

if p1>p2:
    print("El punt més proper a l'origen és p2: ",p2)
elif p1<p2:
    print("El punt més proper a l'origen és p1: ",p1)
elif p1 == p2:
    print("Els dos punts estan a la mateixa distància de l'origen: ", p1)


