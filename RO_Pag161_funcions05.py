# crida a la funció primer

from primer import *
a = int(input("Des de: "))
b = int(input("fins: "))
for n in range(a,b+1):
    if primer(n):
        print("número primer: ",n)