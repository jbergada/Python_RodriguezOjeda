# RO_Pag041_04_decimals_pi.py

comptador = 1
pi_quarts = 0
k = 1

numero_termes = int(input("Número de termes = "))

while comptador != numero_termes :
    if comptador%2 == 1:
        pi_quarts = pi_quarts + (1/k)
    else:
        pi_quarts = pi_quarts - (1/k)
    comptador = comptador + 1
    k = k + 2
    pi = 4 * pi_quarts

print("Aproximació del número pi = ", pi)