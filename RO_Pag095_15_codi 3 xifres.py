#RO_Pag095_15_codi 3 xifres.py

numero = 731

numero1 = numero // 100
numero2 = numero % 100

numero3 = numero2 // 10
numero4 = numero2 % 10

numero5 = (numero1 * numero3) % 10

if numero4 == numero5:
    print("codi vàlid ")
else:
    print("codi NO vàlid ")
    
    