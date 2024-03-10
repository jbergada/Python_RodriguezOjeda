# RO_Pag041_03_Fibonacci.py
# Sèrie de Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

numeros = 8
serie = 0
anterior = 0
seguent = 1
suma = 1

print(numeros+1, "primers números de la sèrie i suma: \n")
print(" serie             suma ")
print("------------------------")
for comptador in range(1, numeros+1):
    if comptador == 1 :
        print("   ", serie + 1, "           ", suma)
    serie = anterior + seguent
    anterior = seguent
    seguent = serie
    suma = serie + suma
    print("   ", serie, "         "," ", suma)
print("\nsuma dels", numeros+1, "primers numeros de la sèrie = ",suma)

    
