# RO_Pag028_if.py

# n = número de llantes
# p = preu inicial
# t = preu a pagar

n = int(input("Número de llantes n = "))
p = float(input("Preu de catàleg de la llanta en € = "))

if n > 4 :
    t = (p - 0.1 * p) * n
else:
    t = n * p
print("Preu a pagar en € = ", t)

