#RO_Pag095_13_if_nomina.py

hores_Joan = float(input("hores Joan= "))
hores_Pere = float(input("hores Pere= "))
hores_Josep = float(input("hores Josep= "))

sou_hora_Joan= 16
sou_hora_Pere= 13
sou_hora_Josep= 16

sou_brut_Joan = hores_Joan * sou_hora_Joan
sou_brut_Pere = hores_Pere * sou_hora_Pere
sou_brut_Josep = hores_Josep * sou_hora_Josep

if sou_brut_Joan <= 3000:
    nomina_Joan = sou_brut_Joan * 0.8
elif sou_brut_Joan > 3000 and sou_brut_Joan <= 5000 :
    nomina_Joan = sou_brut_Joan * 0.75
elif sou_brut_Joan > 5000:
    nomina_Joan = sou_brut_Joan * 0.7

if sou_brut_Pere <= 3000:
    nomina_Pere = sou_brut_Pere * 0.8
elif sou_brut_Pere > 3000 and sou_brut_Pere <= 5000:
    nomina_Pere = sou_brut_Pere * 0.75
elif sou_brut_Pere > 5000:
    nomina_Pere = sou_brut_Pere * 0.7

if sou_brut_Josep <= 3000:
    nomina_Josep = sou_brut_Josep * 0.8
elif sou_brut_Josep > 3000 and sou_brut_Josep <= 5000:
    nomina_Josep = sou_brut_Josep * 0.75
elif sou_brut_Josep > 5000:
    nomina_Josep = sou_brut_Josep * 0.7

print("sou brut Joan ",sou_brut_Joan)
print("sou brut Pere ",sou_brut_Pere)
print("sou brut Josep ",sou_brut_Josep)
print("nomina Joan= ",nomina_Joan)
print("nomina Pere= ",nomina_Pere)
print("nomina Josep= ",nomina_Josep)

if nomina_Joan == nomina_Pere == nomina_Josep:
    print("El Joan, el Josep i el Pere cobren el mateix")
    
elif nomina_Joan == nomina_Pere:
    if nomina_Joan > nomina_Josep:
        print("El Joan i el Pere cobren la nòmina més gran")
    else:
        print("El Josep cobra la nòmina més gran")
elif nomina_Joan == nomina_Josep:
    if nomina_Joan > nomina_Pere:
        print("El Joan i el Josep cobren la nòmina més gran")
    else:
        print("El Pere cobra la nòmina més gran")
elif nomina_Pere == nomina_Josep:
    if nomina_Pere > nomina_Joan:
        print("El Pere i el Josep cobren la nòmina més gran")
    else:
        print("El Joan cobra la nòmina més gran")

elif nomina_Joan > nomina_Pere and nomina_Joan > nomina_Josep:
    print("El Joan cobra al nòmina més gran ")
elif nomina_Pere > nomina_Joan and nomina_Pere > nomina_Josep:
    print("El Pere cobra la nòmina més gran ")
elif nomina_Josep > nomina_Pere and nomina_Josep > nomina_Joan:
    print("El Josep cobra la nòmina més gran")


    
    