#RO_Pag071_interes.py

from math import *

print("Menú ")
print("======")

print(" 1= n= dipòsits mensuals realitzats ")
print(" 2= p= valor de cada dipòsit mensual ")
print(" 3= x= valor nominal de l'interès mensual ")

print("dipòsit mensual ", end="")
p = float(input()) 

print("interès mensual = ", end="")
x = float(input())

print("número de dipòsits mensuals efectuats = ", end="")
n = int(input())

a = p * ((pow(1+x,n)-1)/x)

print("valor acumulat = ", a)

#p = a / ((pow(1+x,n)-1)/x)
#print("valor de cada dipòsit mensual = ", p)