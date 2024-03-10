# RO_Pag038_bucles_suma imparells_bis.py
#import time
#from time import sleep

numero_imparells = 10

suma_imparells = 0

for i in range (1,numero_imparells):
    imparell = 2 * i - 1 # convertim el número a imparell
    suma_imparells = suma_imparells + imparell
    print("suma imparells = ", suma_imparells)
    #time.sleep(5)
    #sleep(5)

suma_imparells = numero_imparells ** 2
print("suma imparells = ", suma_imparells)

"""
numero_imparells = 10
suma_imparells = 0
i = 1
while i <= numero_imparells :
    imparell = 2 * i - 1
    suma_imparells = suma_imparells + imparell
    print("suma imparells = ", suma_imparells)
    i = i + 1
"""   

