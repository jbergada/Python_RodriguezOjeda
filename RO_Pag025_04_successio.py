# RO_Pag025_04_successio.py

# u = a + (n-1) * r ; terme enèssim (últim) de la progressió

# a = primer terme ; n = número de termes ; r = raó

u = float(input("valor de l'enèssim terme = "))
a = float(input("valor del primer terme = "))
n = int(input("número de termes = "))

r = (u-a) / (n-1)

print("la raó r val = ", r)
