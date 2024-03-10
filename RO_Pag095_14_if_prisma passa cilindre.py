# RO_Pag095_14_if_prisma passa cilindre.py

from math import *

x = float(input("valor del costat x del prisma: "))
y = float(input("valor del costat y del prisma: "))
z = float(input("valor del costat z del prisma: "))

d = 10
d1 = sqrt(pow(x,2)+pow(y,2))
d2 = sqrt(pow(x,2)+pow(z,2))
d3 = sqrt(pow(y,2)+pow(z,2))

if d >= d1 or d >= d2 or d >= d3:
    print(" El prisma passa pel forat ")
else:
    print(" El prisma no passa pel forat ")