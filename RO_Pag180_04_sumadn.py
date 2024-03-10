#RO_Pag180_04_sumadn.py
"""4. Escriba una función sumad(n) que entregue la suma de las cifras
de un número dado n. Con esta función escriba un programa que genere 10
números aleatorios entre 1 y 100 y encuentre cual de ellos tiene
la mayor suma de sus cifras."""
from random import randint
def sumad(n):
    suma = 0
    n = str(n)
    #print (n)
    #longitud = len(n)
    for x in n:
        suma = suma + int(x)
    return suma

def aleatori():
    print()
    lista=[]
    max = 0
    ale_num = 0
    for numero in range(0,10):
        aleatorio = randint(1,101)
        print(aleatorio)
        
        print("la suma dels numeros es: ",sumad(aleatorio))
        lista.append(sumad(aleatorio))
        if sumad(aleatorio) > max:
            max = sumad(aleatorio)
            ale_num = aleatorio
    print("suma major =",max, "del numero: ", ale_num )
    
    print (lista)
    count = 0
    for i in lista:
        #print (i)
        if (i == max):
            count = count +1
    if (count >= 2):
        print("n'ha trobat un de repetit")
        
    #print("números de suma mayor: ",ale_num, "endl=(,))
    
    return # no cal, perquè imprimeixo dins la funció
    
aleatori()  
    
'''       
long = sumad(333)
print(long)
aleatoris = aleatori()
print(aleatoris)
'''
