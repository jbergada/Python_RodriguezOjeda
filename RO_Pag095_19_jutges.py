#RO_Pag095_19_jutges.py

j1 = int(input("vot jutge 1 (1=favorable , 0 = eliminat): "))
j2 = int(input("vot jutge 1 (1=favorable , 0 = eliminat): "))
j3 = int(input("vot jutge 1 (1=favorable , 0 = eliminat): "))

if j1 == 0 and j2 == 1 and j3 == 1:
    print(" CONTINUA")
elif j1 == 1 and j2 == 0 and j3 == 1:
    print("CONTINUA")
elif j1 == 1 and j2 == 1 and j3 == 0:
    print("CONTINUA")
elif j1 == 1 and j2 == 1 and j3 == 1:
    print("CONTINUA")
else:
    print("ELIMINAT")
    
