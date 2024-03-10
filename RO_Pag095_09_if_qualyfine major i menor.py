#RO_Pag095_03_if_diagonal major.py
from math import *

qualyfine1 = float(input("Introdueix la qualyfine 1 = "))
qualyfine2 = float(input("Introdueix la qualyfine 2 = "))
qualyfine3 = float(input("Introdueix la qualyfine 3 = "))

if qualyfine1 == qualyfine2 and qualyfine2 == qualyfine3 :
    print("totes les qualyfines són iguals i de valor", qualyfine1)
elif qualyfine1 == qualyfine2:
    if qualyfine1 > qualyfine3:
        print("Les qualyfines més grans són qualyfine1 = qualyfine2 = ",qualyfine1)
        print("La qualyfine més petita és ", qualyfine3)
    else:
        print("La qualyfine més gran és qualyfine3 = ",qualyfine3)
        print("Les qualyfines més petites són qualyfine1 i qualyfine2 = ",qualyfine1)
        
elif qualyfine1 == qualyfine3:
    if qualyfine1 > qualyfine2:
        print("Les qualyfines més grans són qualyfine1 = qualyfine3 =", qualyfine1)
        print("La qualyfine més petita és = ", qualyfine2)
    else:
        print("La qualyfine més gran és qualyfine2= ", qualyfine2)
        print("Les qualyfines més petites són qualyfine1 i qualyfine3= ",qualyfine1)
        
elif qualyfine2 == qualyfine3:
    if qualyfine2 > qualyfine1:
        print("Les qualyfines més grans són qualyfine2 = qualyfine3 =", qualyfine2)
        print("La qualyfine més petita és qualyfine1 = ", qualyfine1)
    else:
        print("La qualyfine més gran és qualyfine1= ", qualyfine1)
        print("Les qualyfines més petites són qualyfine2 i qualyfine3= ", qualyfine2)
        
elif qualyfine1 > qualyfine2 and qualyfine2 > qualyfine3:
    print("La més gran és qualyfine1 = ", qualyfine1)
    print("La més petita és qualyfine3 = ", qualyfine3)
elif qualyfine1 > qualyfine3 and qualyfine3 > qualyfine2:
    print("La més gran és qualyfine1 = ", qualyfine1)
    print("La més petita és qualyfine2 = ", qualyfine2)
    
elif qualyfine2 > qualyfine1 and qualyfine1 > qualyfine3:
    print("La més gran és qualyfine2 = ", qualyfine2)
    print("La més petita és qualyfine3 = ", qualyfine3)
elif qualyfine2 > qualyfine3 and qualyfine3 > qualyfine1:
    print("La més gran és qualyfine2 = ", qualyfine2)
    print("La més petita és qualyfine1 = ", qualyfine1)
    
elif qualyfine3 > qualyfine2 and qualyfine2 > qualyfine1:
    print("La més gran és qualyfine3 = ", qualyfine3)
    print("La més petita és qualyfine1 = ", qualyfine1)
elif qualyfine3 > qualyfine1 and qualyfine1 > qualyfine2:
    print("La més gran és qualyfine3 = ", qualyfine3)
    print("La més petita és qualyfine1 = ", qualyfine2)