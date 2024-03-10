# RO_Pag042_ejemplo2.py
# a, b, c números sencers

t = 0

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a < b :
    t = a + b
elif c > b :
    t = b - c
elif c <= b:
    t = a + b

print("a = ", a , "  t = ", t)
print("b = ", b , "  t = ", t)
        