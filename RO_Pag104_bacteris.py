#RO_Pag104_bacteris

x=int(input('Ingressa la quantitad inicial '))
m=int(input('Ingressa la quantitad màxima '))
d=0;
while x<=m:
    x=2*x
    d=d+1
    print(d,  x)
print('La quantitat excedeix al màxim en el dia:', d)


