#RO_Pag157_funcions.py

def f(x):
    y = 2 * x**2 + 1
    return y
def g(x):
    y = 3 * x**3 + 5
    return y


for x in range(0,5):
    y = f(x)
    print(x,y)

print("")

for x in range(0,5):
    y = g(x)
    print(x,y)   