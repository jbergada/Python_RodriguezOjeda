#RO_Pag146_04_mcd.py

a = int(input("Introdueix el número a : "))
b = int(input("Introdueix el número b : "))

major = 0
if a>= b :
    major = a
else:
    major = b
mcd = 0   
numero = 1
while numero >=1 and numero <= major:
    if a%numero == 0 and b%numero == 0 :
        mcd = numero
    numero = numero + 1
print("mcd de ",a, "i ",b," = ",mcd)


