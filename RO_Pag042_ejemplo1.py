# RO_Pag042_ejemplo1.py
# a, b, c, números sencers

a = int(input("Introdueix el número a = "))
b = int(input("Introdueix el número b = "))
c = int(input("Introdueix el número c = "))

if a < b :
    if b > c :
        print("a = ", a)
print("b = ", b)
print("c = ", c)

print(" ")

if a < b and b > c :
    print("a = ", a)
print("b = ", b)
print("c = ", c)