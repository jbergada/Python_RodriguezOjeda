# RO_Pag032_decisions5.py

quali_1 = float(input("primera quali = "))
quali_2 = float(input("segona quali = "))
quali_3 = float(input("tercera quali = "))

# si posem la inquació >= detecta el número mes gran, encara que n'hi hagi d'iguals

if quali_1 >= quali_2 :
    if quali_1 >= quali_3 :
        print("major quali = ", quali_1)
elif quali_2 >= quali_3 :
    if quali_2 >= quali_1 :
        print("major quali = ", quali_2)
elif quali_3 >= quali_1 :
    if quali_3 >= quali_2 :
        print("major quali = ", quali_3)
