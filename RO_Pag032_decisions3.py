# RO_Pag032_decisions3.py

codi_p = int(input(" Menú => 1 : ºF -> ºC ; 2 : ºC -> ºF "))

if codi_p == 1 :
    temperatura = float(input("Temperatura en ºF = "))
    graus_Celsius = 5/9 * (temperatura - 32)
    print(temperatura, "ºF són ", graus_Celsius, "ºC ")
elif codi_p == 2 :
    temperatura = float(input("Temperatira en ºC = "))
    graus_Fahrenheit = 32 + 9/5 * temperatura
    print(temperatura, "ºC són ", graus_Fahrenheit, "ºF ")
    
# Si posem un 3 al menú, el programa NO entra al if   
