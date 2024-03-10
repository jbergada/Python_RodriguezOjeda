#RO_Pag115_primers.py

while True:
    numero = int(input("Introdueix el número =  "))
    if numero == 1 or numero == 2:
        print("El número ", numero, " és primer")   
    i = 2
    while i < numero:
        
        if numero%i == 0:
            print("El número ", numero, " no és primer")
            i = numero
            
        elif numero%i != 0:
            i = i + 1
            if i == numero:
                print("El número ", numero, " és primer")
    
            


        
        
        
        