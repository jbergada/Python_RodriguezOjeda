#RO_Pag104_Suma de quadrats.py

n=int(input('Ingressa el valor final: '))
s=0
i=1
while i<=n:
    c=i**2
    s=s+c
    print('suma ', i, 'és: ', s)
    i=i+1
    
print('La suma és: ', s)
