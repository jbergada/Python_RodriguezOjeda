# RO_Pag112_suma_imparells.py

n=int(input("Ingressa la quantitat d'imparells:   "))
s=0
imp=1
for i in range(n):
    s=s+imp
    imp=imp+2
if s==n**2:
    print('Verdader')
else:
    print('Fals')
