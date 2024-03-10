# RO_Pag041_02_recompte_vots.py

numero_vots = 10
sis = 0
nos = 0
#nuls = 0

for comptador in range(1, numero_vots+1, 1):
    print("vot ", comptador, " = ", end= " ")
    valor_vot = int(input(""))
    if valor_vot == 1 :
        sis = sis + 1
    elif valor_vot == 0 :
        nos = nos + 1
    #else:
        #nuls = nuls + 1
        

print("vots afirmatius = ", sis)
print("vots negatius = ", nos)
#print("vots nuls = ", nuls)
    