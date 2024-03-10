#RO_Pag081_3_prisma.py

print("àrea i volum d'un prisma, dades en m")

x = float(input("amplada = "))
y = float(input("profunditat = "))
z = float(input("altura = "))

area = 2 * (x*y + y*z + x*z)
volum = x*y*z

print("area =",area," m2")
print("volum = ",volum, " m3")

