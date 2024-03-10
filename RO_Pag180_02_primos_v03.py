# RO_Pag180_2_primer.py
# En la seccion de librerias llamamos a random, como random es tan grande y solo necesitamos random utilizamos el from
from random import randint

def primer(numero):
    es_numero_primer = False
    k = 1
    if (numero == 1 or numero == 2):
        print("El numero ", numero, "es primer")
        k = k + 1
        es_numero_primer = True
        return es_numero_primer

    while k < numero :
        
        if numero%(numero-k) != 0:
            k = k + 1
            if k == numero - 1:
                print("El número ", numero, "és primer")
                k = numero
                es_numero_primer = True
                return es_numero_primer
        else:
            print("El número ", numero, "no és primer")
            k = numero
            es_numero_primer = False
            return es_numero_primer

def primer_suma(numero):
    es_numero_primer = False
    k = 1
    if (numero == 1 or numero == 2):
        #print("El numero ", numero, "es primer")
        k = k + 1
        es_numero_primer = True
        return es_numero_primer

    while k < numero :
        
        if numero%(numero-k) != 0:
            k = k + 1
            if k == numero - 1:
                #print("El número ", numero, "és primer")
                k = numero
                es_numero_primer = True
                return es_numero_primer
        else:
            #print("El número ", numero, "no és primer")
            k = numero
            es_numero_primer = False
            return es_numero_primer

def random():
    #print(randint(1,100))
    sortida = randint(1,100) # sortida es local
    #print("sortida dins de la funció: ", sortida)
    return sortida
    
#primer(11)
#random()
'''
a = random()
b = random()
primer(a)
primer(b)
suma = a + b
c = primer(suma)
#print (a,b)
'''
control = True
while control == True:
    a = random()
    b = random()
    primer(a)
    primer(b)
    if primer(a) == True and primer(b) == True:
        suma = a + b
        c = primer_suma(suma)
        if c == True:
            #print("la suma és un número primer")
            control = False
        else:
            print("la suma no dona un primer")
print("la suma dona un primer",suma)
    
 