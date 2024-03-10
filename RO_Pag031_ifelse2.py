# RO_Pag031_ifelse2.py

hores = float(input("Hores treballades = "))
preu_hora = float(input("Preu per hora treballada = "))
descompte = float(input("Descomptes per impostos i etc = "))

if hores <= 40:
    nomina = hores * preu_hora - descompte
    
else:
    nomina = (40 * preu_hora) - descompte + (1.5 * preu_hora * (hores - 40))

print("nomina = ", nomina)