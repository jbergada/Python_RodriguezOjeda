# RO_Pag047_Algotitme02.py

n = int(input("n = "))

for i in range (1, n+1, 1):
    k = 2 * i - 1
    print("i = ", i , "k = ", k)

print(" ")

i = 1
while i <= n :
    k = 2 * i - 1
    print("i = ", i , "k = ", k)
    i = i + 1
    
print(" ")

i = 1
control = True
while control == True:
    k = 2 * i - 1
    print("i = ", i , "k = ", k)
    i = i + 1
    while i > n:
        control == False
        
    