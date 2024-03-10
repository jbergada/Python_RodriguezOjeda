#RO_Pag181_factorial.py
from random import randint
def factorial(n):
    N = n # deso una còpia del número a calcular el factorial
    resultat = n
    while n > 2 :
        resultat = resultat * (n-1)
        n = n - 1
        #print(resultat)
    print("factorial de",N,"=",resultat)
    return resultat

k = randint(1,10)
print("k = ",k)
suma = 0
for k in range(1,k+1):
    result = factorial(k) # la variable result ens la podem estalviar
    suma = suma + result
    print("factorial de ",k,"=",result)
print("Suma dels factorials de 1 a k =",suma)


