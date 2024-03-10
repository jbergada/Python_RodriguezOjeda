#RO_Pag071_interes.py

from math import *

print("dipòsit mensual en euros = ", end="")
aportacio_mensual = float(input()) 

print("interès mensual = ", end="")
i_mensual = float(input())

print("número de dipòsits mensuals efectuats = ", end="")
numero_diposits = int(input())

mes = aportacio_mensual + i_mensual*aportacio_mensual
print("capital mes 1 = ", mes)
for i in range(2, numero_diposits+1):
    
    if i == numero_diposits:
        mes_seguent = (mes + aportacio_mensual)
        print("capital mes ",numero_diposits, " =", mes_seguent)
    else:
        mes_seguent = (mes + aportacio_mensual)+i_mensual*(mes+aportacio_mensual)
        mes = mes_seguent
        print("capital mes ",i," =", mes_seguent)
        
print("capital final = ", mes_seguent)