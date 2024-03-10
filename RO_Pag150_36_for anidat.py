#RO_Pag150_36_for anidat.py

from math import *

n = 1
m = 2
sol = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        sol = pow(i,2)+pow(j,2)+(i*j) + sol
print("solució = ", sol)