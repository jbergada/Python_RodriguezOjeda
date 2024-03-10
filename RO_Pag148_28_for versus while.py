#RO_Pag148_28_for versus while.py

n = int(input("Introdueix una dada: "))
s = 0
for i in range(1,n):
    s = s + i**2
    print(s)
    
print()

i = 1
s = 0
while i < n:
    s = s + i**2
    i = i + 1
    print(s)