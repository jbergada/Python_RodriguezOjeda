#RO_Pag180_03_perfecte.py


def divisors_num(x):
    #llista = []
    suma = 0
    for i in range(x-1,0,-1):
        a = x%i
        if a == 0:
            #llista.append(i)
            suma = suma + i
            #print(i)
            
    if(suma == x):
        print(suma)
        print("El número",x, "és perfecte")
    #else:
        #print("El número",x, "no és perfecte")

for j in range(1,10000):
    divisors_num(j)
