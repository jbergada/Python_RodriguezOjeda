#RO_Pag095_4_if_parell o imparell.py

numero1 = 87

xifra_1a = numero1 // 10
xifra_2a = numero1 % 10
suma = xifra_1a + xifra_2a

if suma % 2 == 0:
    print("número = ", suma, "és parell")
else:
    print("número = ", suma, "és imparell")