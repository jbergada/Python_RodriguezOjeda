#RO_Pag155_funcions01.py
from math import *

def f(x):
    y = 2* pow(x,2) +1
    y = int(y)
    print(y)
    return 

def g(a):
    b = 2* pow(a,2)
    return b

# programa principal

for i in range(5):
    y = f(i)
    print(i,y)

b = g(2) # s'executa la darrera vegada
print(b)