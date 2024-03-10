# RO_Pag044_ejemplo3_bis.py

a= int(input("a = "))
b= int(input("b = "))
c= int(input("c = "))

r = 0

while not(a < b or c <= 0) :
    if b%2 != 0 :
        r = r + c
        print("r = ", r)
    b = b + 1
    print("b = ", b)

print("r = ", r)
