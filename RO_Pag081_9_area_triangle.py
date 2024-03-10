#RO_Pag081_9_area_triangle.py

from math import *

a = 4
b = 2

c = 2
d = 4

x = sqrt(pow((c-a),2) + pow((d-b),2))

y = sqrt(pow(a,2)+pow(b,2))

z = sqrt(pow(c,2)+pow(d,2))

t = (x+y+z)/2

s = sqrt(t*(t-x)*(t-y)*(t-z))

print("s = ",s)
         