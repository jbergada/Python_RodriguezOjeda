# RO_Pag041_05_serie_pi.py

a = 1
serie = a ** a
termes_sumats = 1

x = int(input("Introdueix un número sencer x = ")) 

while serie <= x :
    termes_sumats = termes_sumats + 1
    a = a + 1
    serie = serie + a ** a

print("Termes sumats per superar el número entrat x = ", termes_sumats)

