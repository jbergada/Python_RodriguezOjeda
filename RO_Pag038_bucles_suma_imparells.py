# RO_Pag038_bucles_suma_imparells.py

"""
for k in range (1,10,1):
    print(k)

n = [2, 5, 4, 7, 6]

print("\n")

for i in n:
    print(i)
"""

numero_imparell = int(input("Número de números imparells a sumar ? "))
suma_imparells = 0

for i in range (1, numero_imparell+1):
    imparell = 2 * i - 1 # convertim el número a imparell
    suma_imparells = suma_imparells + imparell
    print("imparell =  ", imparell, "suma_imparells = ", suma_imparells)

if suma_imparells == numero_imparell ** 2 :
    print("S'acompleix que, donat un número imparell, si sumem els primers numero_imparell números, ")
    print("el resultat és el número imparell al quadrat ")
else:
    print("No s'acompleix que, donat un número imparell, si sumem els primers numero_imparell números, ")
    print("el resultat és el número imparell al quadrat ")
    

numero_imparells = 10
suma_imparells = 0
i = 1
while i <= numero_imparells :
    imparell = 2 * i - 1
    suma_imparells = suma_imparells + imparell
    print("suma imparells = ", suma_imparells)
    i = i + 1
if suma_imparells == numero_imparell ** 2 :
    print("S'acompleix que, donat un número imparell, si sumem els primers numero_imparell números, ")
    print("el resultat és el número imparell al quadrat ")
else:
    print("No s'acompleix que, donat un número imparell, si sumem els primers numero_imparell números, ")
    print("el resultat és el número imparell al quadrat ")
    

#print("i = ", i)
