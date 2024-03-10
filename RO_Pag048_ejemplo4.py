# RO_Pag048_ejemplo4.py

a = int(input("a = "))
b = int(input("b = "))

if a > 0 :
    if b < 100 :
        t = 2 * a + b
        #print("t = ", t)
else: # a < 0 => t = 0
    t = 0
    #print("t = ", t)
print("t = ", t)
