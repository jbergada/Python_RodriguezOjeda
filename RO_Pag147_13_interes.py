#RO_Pag147_13_interes.py

from math import *

print("Menú ")
print("======")

print(" 1= a= valor acumulat ")
print(" 2= x= valor nominal de l'interès mensual ")
print(" 3= n= número de dipòsits mensuals efectuats ")

print("valor acumulat ", end="")
a = float(input()) 

print("interès mensual = ", end="")
x = float(input())

print("número de dipòsits mensuals efectuats = ", end="")
n = int(input())

#a = p * ((pow(1+x,n)-1)/x)

#print("valor acumulat = ", a)

p = a / ((pow(1+x,n)-1)/x)
print("valor de cada dipòsit mensual = ", p)

