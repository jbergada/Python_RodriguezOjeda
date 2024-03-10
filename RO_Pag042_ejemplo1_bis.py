#RO_Pag42_ejemplo1.py

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a < b :
    if c < b:
        print("a = ", a, end= "")
print("  b =", b, "  c =", c)

if a < b and c < b :
    print("a = ", a, end = "")
print("  b =", b, "  c =", c)

