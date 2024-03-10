# RO_Pag146_11_Fibonacci.py

anterior = 0
numero = 1

i = 1

print("Serie de Fibonacci = ", numero, ", ", end="")
while i < 9:
    
    seguent = anterior + numero
    anterior = numero
    numero = seguent
    i = i + 1
    print(seguent,", ",end="")
