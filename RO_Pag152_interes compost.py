#RO_Pag152_interes compost anual.py

#Fórmula de l'interès compost
from math import *
sortida=False
while not sortida:
    print('1) Valor acumulat')
    print('2) Dipòsit mensual')
    print('3) Número de dipòsits')
    print('4) Sortir')
    opc=input('Escull una opció: ')
    if opc=='1':
        p=float(input('Valor del dipòsit mensual: '))
        n=int(input('Número de dipòsits mensuals: '))
        x=float(input('Interès anual en percentatge: '))
        m=0.01*x/12
        a=p*(pow((1+m),n)-1)/m
        print('Valor acumulado: ',a)
    elif opc=='2':
        a=float(input('Valor acumulat: '))
        n=int(input('Número de depósits mensuals: '))
        x=float(input('Interès anual en percentatge: '))
        m=0.01*x/12;
        p=a*m/((1+m)**n-1);
        print('Quota mensual: ',p)
    elif opc=='3':
        a=float(input('Valor acumulat: '))
        p=float(input('Valor del dipòsit mensual: '))
        x=float(input('Interés anual en percentatge: '))
        m=0.01*x/12;
        n=log(a*m/p+1)/log(1+m);
        print('Número de dipòsits: ',n)
    elif opc=='4':
        salida=True
