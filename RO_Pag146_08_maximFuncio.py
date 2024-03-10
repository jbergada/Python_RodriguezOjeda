# RO_Pag146_08_maximFuncio.py

from math import *



x = 1.0

while x <= 4:
    fx = sin(x) + log(x)
    print("Per a x = ",round(x,3), "f(x) = sin(x) + ln(x) = ",round(fx,7))
    x = x + 0.1
    
    
