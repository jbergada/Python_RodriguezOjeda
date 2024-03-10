# RO_Pag047_ejemplo3_while.py

s = 0
x = int(input("x = "))

while s < 100 :
    if x > 0 and x < 10 :
        s = s + x
        print("s = ", s)
print("s = ", s)

s = 0
control = True
while control == True:
    if x > 0 and x < 10:
        s = s + x
        print("s =", s)
    while s >= 100:
        control == False
print("s = ", s)
        
        