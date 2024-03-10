# RO_Pag041_06_escacs.py

a = 1
serie = 2 ** a
caselles = 1
print(serie)

while caselles <= 63:
    serie = serie + 2 ** a
    print(serie)
    a = a + 1
    caselles = caselles + 1

print("Suma dels grans de blat que caben en el taulell d'escacs = ", serie)
print("kg de blat que caben en el taulell d'escacs = ", serie/20000)
print("Tonelades de blat que va caler satisfer = ", (serie/20000)/1000)

