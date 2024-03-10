#RO_Pag157_funcio.py

def f(x):
    y = 2 * x**2 + 1
    return y

#Programa que fa servir la funció f
#Programa principal

for x in range(1,5):
    y = f(x)
    print(x,y)