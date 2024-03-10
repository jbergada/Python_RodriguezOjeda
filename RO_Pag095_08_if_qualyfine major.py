# RO_08_if_qualyfine major.py

from math import *

print("       estudiant 1       ")
print("=========================")

q1 = int(input("qualificació 1 = "))
q2 = int(input("qualificació 2 = "))
q3 = int(input("qualificació 3 = "))

if q1 >= q2 and q2 >= q3:
    qualyfine = q1 + q2
    print("qualyfine = ", qualyfine)

elif q1 >= q3 and q3 >= q2:
    qualyfine = q1 + q3
    print("qualyfine = ", qualyfine)

elif q2 >= q1 and q1 >= q3:
    qualyfine = q2 + q1
    print("qualyfine = ", qualyfine)

elif q2 >= q3 and q3 >= q1:
    qualyfine = q2 + q3
    print("qualyfine = ", qualyfine)

elif q3 >= q2 and q2 >= q1:
    qualyfine = q3 + q2
    print("qualyfine = ", qualyfine)

elif q3 >= q1 and q1 >= q2:
    qualyfine = q3 + q1
    print("qualyfine = ", qualyfine)

qualyfine1 = qualyfine

print("                         ")
print("       estudiant 2       ")
print("=========================")

q1 = int(input("qualificació 1 = "))
q2 = int(input("qualificació 2 = "))
q3 = int(input("qualificació 3 = "))

if q1 >= q2 and q2 >= q3:
    qualyfine = q1 + q2
    print("qualyfine = ", qualyfine)

elif q1 >= q3 and q3 >= q2:
    qualyfine = q1 + q3
    print("qualyfine = ", qualyfine)

elif q2 >= q1 and q1 >= q3:
    qualyfine = q2 + q1
    print("qualyfine = ", qualyfine)

elif q2 >= q3 and q3 >= q1:
    qualyfine = q2 + q3
    print("qualyfine = ", qualyfine)

elif q3 >= q2 and q2 >= q1:
    qualyfine = q3 + q2
    print("qualyfine = ", qualyfine)

elif q3 >= q1 and q1 >= q2:
    qualyfine = q3 + q1
    print("qualyfine = ", qualyfine)

if qualyfine1 > qualyfine:
    print("L'estudiant 1 té millor qualyfine")
elif qualyfine1 < qualyfine:
    print("L'estudiant 2 té millor qualyfine")
else:
    print("Els dos estudiants tenen la mateixa qualyfine")