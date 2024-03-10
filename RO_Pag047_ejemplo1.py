# RO_Pag047_Algotitme01.py

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

x = 0
y = 0

if not(a < 2 and b > 1) or (c > 3) :
    x = a + b
else:
    y = b - c

print("x = ", x, "  y = ", y)

if (a >= 2 or b <= 1) or (c > 3) :
    x = a + b
else:
    y = b - c

print("x = ", x, "  y = ", y)

if a >= 2 :
    x = a + b
elif b <= 1 :
    x = a + b
elif c > 3 :
    x = a + b
else:
    y = b - c

print("x = ", x, "  y = ", y)