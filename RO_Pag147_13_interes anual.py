#RO_Pag147_13_interes anual.py

from math import *

print("Menú ")
print("======")

print(" 1= p = cost màquina ")
print(" 2= x= valor nominal de l'interès anual ")
print(" 3= n= número de dipòsits mensuals efectuats ")

print("cost màquina ", end="")
p = float(input()) 

print("número d'anys = ", end="")
n = int(input())

x = 0.01
while x < 0.1:
    a = p * (x * pow(1+x,n))/ (pow(1+x,n)-1)
    print("Cuota anual = ",a)
    print("valor acumulat per x = ",x, "= ", a*n)
    x = x + 0.01
   
interes = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
for i in interes:
    a = p * (i * pow(1+i,n))/ (pow(1+i,n)-1)
    print("Cuota anual = ",a)
    print("valor acumulat per x = ",i, "= ", a*n)
