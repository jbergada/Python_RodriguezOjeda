# RO_Pag048_ejemplo5.py

a = int(input("a = "))
b = int(input("b = "))

if a < 0:
    if b < 0 :
        b = 2 * b
        print("a = ", a)
        print("b = ", b)
while a < b:
    a = a + 1
    b = b - 1 
    print("a = ", a)
    print("b = ", b)


