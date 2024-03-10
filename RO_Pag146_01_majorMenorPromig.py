#RO_Pag146_01_majorMenorPromig.py

n = int(input("Número de paquets = "))

major = 0
suma = 0

i = 1
while i <= n:
    print("Pes del paquet ",i,"=", end="")
    pes = float(input())
    suma = suma + pes
    if i == 1:
        menor = pes
    else:
        if pes < menor:
            menor = pes
    if pes > major:
        major = pes
    i = i + 1
promig = suma / n
print("Pes del paquet més gran: ", major)
print("Pes del paquet més petit: ", menor)
print("Promig = ", promig)

major = 0
suma = 0

for i in range (1,n+1):
    print("Pes del paquet ",i,"=", end="")
    pes = float(input())
    suma = suma + pes
    if i == 1:
        menor = pes
    else:
        if pes < menor:
            menor = pes
    if pes > major:
        major = pes
promig = suma / n
print("Pes del paquet més gran: ", major)
print("Pes del paquet més petit: ", menor)
print("Promig = ", promig)   
    
