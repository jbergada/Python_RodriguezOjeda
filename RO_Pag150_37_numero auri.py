#RO_Pag150_37_numero auri.py
n = int(input("n = "))
print("Parelles de números (a,b) entre 1 i n")
print("=====================================")
parelles_auries = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        print("(a,b)= ", "(", a, b,")")
        if (a+b)/a == a/b:
            print("La parella (", a, b,") respon al número auri")
            parelles_auries = parelles_auries + 1
if parelles_auries == 0:
    print("No hi ha cap parella (a,b) àuria") 