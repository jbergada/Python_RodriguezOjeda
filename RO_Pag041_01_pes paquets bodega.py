# RO_Pag041_01_pes paquets bodega.py

num_paquets = 1
pes_maxim = 0

# resolem amb while

while num_paquets != 10:
    print("Pes del paquet ",num_paquets, " en kg = ", end = " ")
    pes_paquet = float(input())
    if pes_paquet > pes_maxim :
        pes_maxim = pes_paquet
    num_paquets = num_paquets + 1

print("El pes del paquet més gran val: ", pes_maxim)

# resolem amb for

num_paquets = 10
pes_maxim = 0

for comptador in range (1, num_paquets+1, 1):
    print("Pes del paquet ",comptador, " en kg = ", end = " ")
    pes_paquet = float(input())
    if pes_paquet > pes_maxim :
        pes_maxim = pes_paquet
    #num_paquets = num_paquets - 1
print("El pes del paquet més gran val: ", pes_maxim)