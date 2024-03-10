# RO_Pag40_repetir_fins_condicio.py

a = True
p = 4 # si p = 0, a serà false i s'atura el bucle
while a == True:
    print("p = ", p)
    if p <= 0 :
        a = False
    p = p - 1
    print(p)
        