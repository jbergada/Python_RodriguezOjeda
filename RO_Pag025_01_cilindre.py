# RO_Pag025_01_cilindre.py

radi = float(input("radi = "))
altura = float(input("altura = "))

area_cilindre = 2 * ( 3.1416 * radi * radi ) + (2 * 3.1416 * radi * altura)
volum = 3.1416 * radi * radi * altura

print("area total = ", area_cilindre)
print("volum = ", volum)
