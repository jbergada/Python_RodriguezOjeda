# RO_Pag042_ejemplo2_bis.py
# a, b, c, números sencers

t = 0

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a < b :
    t = a + b
elif c <= b :
    t = a + b
else :
    t = b - c

print("a = ", a , " t = ", t)
print("b = ", b , " t = ", t)

print(" ")

t = 0

if a < b or c <= b :
    t = a + b
else:
    t = b - c

print("a = ", a , " t = ", t)
print("b = ", b , " t = ", t)
