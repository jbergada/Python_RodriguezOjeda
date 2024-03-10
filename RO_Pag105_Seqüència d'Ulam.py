# RO_Pag105_Sequència d'Ulam.py

x=int(input('Ingressa la dada inicial: '))
while x>1:
    if x%2 == 0:
        x=x//2
    else:
        x=3*x+1
    print(x)
