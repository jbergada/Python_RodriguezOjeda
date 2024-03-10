#RO_Pag095_06_if_kWh.py

kWh = float(input("lectura en kWh = "))
preu_kWh = 0.2
preu_kWh_2 = preu_kWh * 1.05
if kWh > 7700:
    preu = kWh * preu_kWh_2
else:
    preu = kWh * preu_kWh
print("preu a pagar = ",preu)