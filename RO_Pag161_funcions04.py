# RO_Pag161_funcions04.py

def primer(n):
    c = 0
    for i in range(1,n+1):
        if n%i==0:
            c = c + 1
    if c > 2:
        return False
    else:
        return True

a = int(input("Des de: "))
b = int(input("fins: "))
for n in range(a,b+1):
    if primer(n):
        print("número primer: ",n)