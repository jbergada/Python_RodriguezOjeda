#RO_Pag114_divisors.py
#divisors d'un sencer
n = int(input("Introdueix un número senser "))
comptador = 0
for d in range (1, n+1):
    if n%d == 0:
        print("divisor = ", d)
        comptador = comptador + 1
print("Hi ha ", comptador, " divisors exactes")
        
