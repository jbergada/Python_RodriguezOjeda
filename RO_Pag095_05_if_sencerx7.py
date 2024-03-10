#RO_Pag095_05_sencerx7.py

a = float(input("introdueix un número: "))
b = int(a//1) # no cal crear la variable b

if a-b != 0:
    print(a , " no és un número sencer ") 
elif a%7 == 0:
    print(int(a) ," és sencer i múltiple de 7")
elif a%7 != 0:
    print(int(a) , " és sencer però no és múltiple de 7 ")

        