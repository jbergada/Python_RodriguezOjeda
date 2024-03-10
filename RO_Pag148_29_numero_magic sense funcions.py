# RO_Pag148_29_numero_magic sense funcions.py

dia = 20
mes = 4
anY = 1967

suma = dia + mes + anY
unitat = suma % 10
print("unitat = ", unitat)
desena = (suma // 10) % 10
print("desena = ", desena)
centena = (suma // 100) % 10
print("centena = ", centena)
miler = suma // 1000
print("miler = ", miler)

suma_2 = miler + centena + desena + unitat
unitat_2 = suma_2 % 10
print("unitat_2 = ", unitat_2)
desena_2 = suma_2 // 10
print("desena_2 = ", desena_2)

numero_magic = unitat_2 + desena_2
print("numero_magic = ", numero_magic)


