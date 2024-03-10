#RO_Pag148_29_numero_magic.py

def suma_numeros(num):
    str_suma = str(num)
    nova_suma = 0
    for i in str_suma:
        nova_suma = int(i) +nova_suma   
    return nova_suma


# dia = int(input("Introdueix el dia de naixement: "))
# mes = int(input("Introdueix el mes : "))
# anY = int(input("Introdueix l'any : "))
dia = 28
mes = 11
anY = 1989
suma = dia + mes + anY

numero_xifres = len(str(suma))

while (numero_xifres > 1):
    suma = suma_numeros(suma)
    numero_xifres = len(str(suma))

print("numero magic: ", suma)


          
