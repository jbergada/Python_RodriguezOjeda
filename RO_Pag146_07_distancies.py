#RO_Pag146_7_distancies.py
from math import *

print("Ubicació de la fàbrica. Coordenada u = ", end="")
u = float(input())
print("Ubicació de la fàbrica. Coordenada v = ", end="")
v = float(input())
n = 1 # punts de distribució
km = 0

i = 1
while i >= 1 and i <= n:
    
    print("Coordenada x del punt de distribució = ", end="")
    x = float(input())
    print("Coordenada y del punt de distribució = ", end="")
    y = float(input())
    
    h = sqrt(pow((u-x),2) + pow((v-y),2))
    km = km + h
    i = i + 1

print("distància acumulada en km = ", km)


