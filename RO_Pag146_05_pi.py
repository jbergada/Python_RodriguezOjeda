#RO_Pag146_05_pi.py
from math import *

termes = 40000
n = 1
i = 1
pi = 0
while i >=1 and i <= termes:
    if i%2 != 0:
        pi_4 = 1/n
    else:
        pi_4 = -(1/n)
    pi = (pi + pi_4)
    n = n + 2
    i = i + 1
    #print("pi = ", pi*4)
print("pi = ", pi*4)
        
        