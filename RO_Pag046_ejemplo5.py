# RO_Pag046_ejemplo5.py

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a > b :
    while c <= a :
        c = c + 3
        print("c = ", c)
else:
    a = a + 5
    while a <= b + c :
        a = a + 5
        print("a = ", a)
    print ("a = ", a)
print("c = ", c)
    



print("c = ", c)