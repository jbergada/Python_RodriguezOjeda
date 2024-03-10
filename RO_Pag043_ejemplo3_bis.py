# RO_Pag43_ejemplo2.py

t = 0

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a < b or c <= b : # si és més gran que a ó c, suma
    t = a + b
else:
    t = b - c
    
print("a = ",a, "t = ",t)
print("b = ",b, "t = ",t)