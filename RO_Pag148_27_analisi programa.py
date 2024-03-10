# RO_Pag148_27_analisi programa.py

n = int(input("Introdueix una dada: "))

r = 0
while n > 0:
    d = n%2
    n = n//2
    r = 10*r + d
    print(d, n, r)
    