#RO_Pag161_funcions06.py
#Troba parelles de nombres primers
# que la suma sigui suma
from primer import *
suma = int(input("Ingressa la suma:"))
for i in range(suma):
    for j in range(suma):
        a = primer(i)
        b = primer(j)
        #primer(j)
        if a == True and b == True and i+j == suma:
            print("Parell de primers:", i,j)
