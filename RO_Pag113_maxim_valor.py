#RO_Pag113_maxim_valor.py

n=int(input('Quantitat de dades: '))
t=0
for i in range(n):
    x=float(input('Ingressa la següent dada: '))
    if x>t:
        t=x
print('El major valor és: ',t)
