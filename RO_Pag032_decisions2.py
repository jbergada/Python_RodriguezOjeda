# RO_Pag032_decisions2.py

preu_Kwh = float(input("Preu del Kwh = "))
Kwh_consumits = float(input("Kwh consumits = "))

if Kwh_consumits <= 700 :
    preu = Kwh_consumits * preu_Kwh
    print("Preu a pagar = ", preu, " € ")
else:
    preu = 700 * preu_Kwh
    preu = preu + (1 + 0.05) * preu_Kwh * (Kwh_consumits - 700)
    print("Preu a pagar = ", preu, " € ")
    
    

