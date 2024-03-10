#RO_Pag146_06_vots.py

vots = 4

blancs = 0
candidat_1 = 0
candidat_2 = 0
candidat_3 = 0
nuls= 0
resultat = 0

i = 1
while i >= 1 and i <= vots:
    print("resultat vot ", i, " = ", end="")
    resultat = int(input())
    print(i)
    if resultat == 0:
        blancs = blancs + 1
    elif resultat == 1:
        candidat_1 = candidat_1 + 1
    elif resultat == 2:
        candidat_2 = candidat_2 + 1
    elif resultat == 3:
        candidat_3 = candidat_3 + 1
    else:
        nuls = nuls + 1
    i = i + 1
print("candidat_1 = ", candidat_1)
print("candidad_2 = ", candidat_2)
print("candidat_3 = ", candidat_3)
print("vots en blanc = ", blancs)
print("vots nuls = ", nuls)


        
    
