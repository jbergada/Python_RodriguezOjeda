#RO_Pag111_promig.py

n=int(input('Quantitat de dades: '))
s=0
for i in range(n):
    x=float(input('Ingressa la següent dada: '))
    s=s+x
    p=s/n
print('El promig és: ',p)
