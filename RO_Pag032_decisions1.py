# RO_Pag32_decisions1.py

PI = 3.141592 # definim la consrant PI

radi = float(input("Introdueix el radi del cilindre en cm3 = "))
altura = float(input("Introdueix l'alçada en cm = "))

if altura > radi :
    volum = PI * radi**2 * altura
    print("volum = ", volum, " cm3 ")
else:
    area = 2 * (PI * radi **2) + 2 * PI * radi * altura
    print("area = ", area, " cm2 ")
    
