#RO_Pag149_35_for anidat.py

a = int(input("Introdueix a entre 1 i 1000: "))
b = int(input("Introdueix b entre 1 i 1000: "))

for a in range (1,3):
    for b in range (1,10):
        x = 1000 - a
        y = 1000 - b
        suma = x + y
        resta = 1000 - suma
        producte1 = resta * 1000
        producte2 = x * y
        resultat = producte1 + producte2
        if resultat == a * b :
            print("El resultat del producte (a, b)= ", a, b, "= ",a*b,  "és correcte: ", resultat)
        else:
            print("El resultat és incorrecte", resultat)
        
