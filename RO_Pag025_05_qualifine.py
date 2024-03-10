# RO_Pag025_05_qualifine.py

challenge = float(input("quali del challenge sobre 100 = "))
tema = float(input("quali del tema sobre 10 = "))
tasca1 = float(input("quali de la tasca 1 sobre 10 = "))
tasca2 = float(input("quali de la tasca 2 sobre 10 = "))
tasca3 = float(input("quali de la tasca 3 sobre 10 = "))

qualifine = ((tasca1+tasca2+tasca3)/3) + (0.7 * challenge) + (0.2 * 10 * tema)

print("qualifine = ", qualifine)



