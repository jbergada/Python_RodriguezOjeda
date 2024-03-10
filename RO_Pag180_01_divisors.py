#RO_Pag180_01_divisors.py

def divisors(n):
    counter = 0
    divisor = n # n és el dividend
    while divisor > 0:
        if n%(divisor) == 0:
            #print(divisor)
            counter = counter + 1
        divisor = divisor - 1
    #print("número de divisors de ", n ,"= ",counter)
    return counter

#divisor = 96
#comptador = divisors(divisor) # també puc usar counter
#print("número de divisors de ",divisor, " = ",comptador)

maxim = 0
for divisor in range (1,101):
    comptador = divisors(divisor)
    print("número de divisors de ",divisor,"=", comptador)
    if comptador > maxim:
        maxim = comptador
        numero = divisor
print("Número màxim de divisors = ",maxim)

print("números amb el màxim número de divisors:")
for divisor in range (1,101):
    comptador = divisors(divisor)
    if comptador == maxim:
        print(divisor, end=",")
        
        

        