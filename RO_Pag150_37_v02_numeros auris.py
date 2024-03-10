#RO_Pag150_37_v02_numeros auris.py
import math
n = int(input("n = "))
print("Parelles de números (a,b) entre 1 i n")
print("=====================================")
parelles_auries = 0
precisio = 0.01
num_auris = (1+ math.sqrt(5))/2
llista_parelles = []
for a in range(1,n+1):
    for b in range(1,n+1):
        print("(a,b)= ", "(", a, b,")")
        if (num_auris + precisio > a/b) and (num_auris - precisio < a/b):
            print("La parella (", a, b,") respon al número auri")
            llista_parelles.append([a,b])
            parelles_auries = parelles_auries + 1
        
if parelles_auries == 0:
    print("No hi ha cap parella (a,b) àuria") 
else:
    print(llista_parelles)
