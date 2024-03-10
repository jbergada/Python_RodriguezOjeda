# RO_Pag25_03_prisma.py

amplada = float(input("Introdueix l'amplada en metres = "))
altura = float(input("Introdueix l'altura en metres = "))
profunditat = float(input("introdueix la profunditat = "))

area = 2 * (amplada * profunditat + altura * profunditat + amplada * altura)
volum = amplada * profunditat * altura

print("area = ", area, " metres quadrats")
print("volum = ", volum, " metres cúbics")
