#RO_Pag146_02_pesosBodega.py

n = int(input("Número de paquets = "))

menor_10 = 0
mida10_20 = 0
major_20 = 0

i = 1

while i <= n:
    print("Pes del paquet ",i," en kg =", end="")
    pes = float(input())
    if pes < 10:
        menor_10 = menor_10 + 1
    elif pes >=10 and pes <= 20:
        mida10_20 = mida10_20 + 1
    elif pes > 20:
        major_20 = major_20 + 1
    i = i + 1

print("Hi ha ",menor_10, " paquets amb pes menor a 10 kg")
print("Hi ha ",mida10_20, " paquets de mida entre 10 i 20 kg")
print("Hi ha ",major_20, " paquets de mida major de 20 kg")

menor_10 = 0
mida10_20 = 0
major_20 = 0

for i in range (1,n+1):
    print("Pes del paquet ",i," en kg =", end="")
    pes = float(input())
    if pes < 10:
        menor_10 = menor_10 + 1
    elif pes >=10 and pes <= 20:
        mida10_20 = mida10_20 + 1
    elif pes > 20:
        major_20 = major_20 + 1
        
print("Hi ha ",menor_10, " paquets amb pes menor a 10 kg")
print("Hi ha ",mida10_20, " paquets de mida entre 10 i 20 kg")
print("Hi ha ",major_20, " paquets de mida major de 20 kg")