#RO_Pag159_geometria.py
# A = Area ; P = Perímetre ; V = Volum
from math import *

def quadrat(a):
    A = a * a
    P = 4 * a
    print("Àrea = ", A)
    print("Perímetre = ", P)
def triangle(a,b,c,h):
    A = (b * h)/2
    P = a + b + c
    print("Àrea = ", A)
    print("Perímetre = ", P)
def rectangle(a,b):
    A = b * a
    P = 2*(b+a)
    print("Àrea = ", A)
    print("Perímetre = ", P)
def paralelogram(a,b,h):
    A = b * h
    P = 2*(b+a)
    print("Àrea = ", A)
    print("Perímetre = ", P)
def rombe(D,d,a):
    A = (D*d)/2
    P = 4 * a
    print("Àrea = ", A)
    print("Perímetre = ", P)
def estel(D,d,b,a):
    A = (D*d)/2
    P = 2*(b+a)
    print("Àrea = ", A)
    print("Perímetre = ", P)
def trapezi(B,b,a,c,h):
    A = ((B+b)*h)/2
    P = B + b + a + c
    print("Àrea = ", A)
    print("Perímetre = ", P)
def cercle(r):
    A = pi * pow(r,2)
    P = 2 * pi * r
    print("Àrea = ", A)
    print("Perímetre = ", P)
def poligon(b,n,a):
    P = n * b
    A = (P * a)/2
    print("Àrea = ", A)
    print("Perímetre = ", P)
def corona(R,r):
    A = pi * (pow(R,2) + pow(r,2))
    print("Àrea = ", A)
def sector(r,n):
    A = (pi * pow(r,2) *n)/360
    print("Àrea = ", A)
def cub(a):
    A = 6 * pow(a,2)
    V = pow(a,3)
    print("Àrea = ",A)
    print("Volum = ",V)
def cilindre(r,h):
    A = 2 * pi * r * (h + r)
    V = pi * pow(r,2) * h
    print("Àrea = ", A)
    print("Volum = ", V)
def ortoedre(a,b,c):
    A = 2 * (a*b + a*c + b*c)
    V = a * b * c
    print("Àrea = ", A)
    print("Volum = ", V)
def prisma(b,n,a,h):
    Pb = n * b   # perímetre de la base
    Ab = (Pb * a)/2 # àrea de la base
    A = Pb * (h + a)
    V = Ab * b
    print("Àrea = ", A)
    print("Volum = ", V)
def con(r,g,h):
    A = pi * r * (r + g)
    V = (pi * pow(r,2) * h) / 3
    print("Àrea = ", A)
    print("Volum = ", V)
def tronc_con(r,R,g,h):
    A = pi * (g * (r + R) + pow(r,2) + pow(R,2))
    V = pi * h + (pow(r,2) + pow(R,2) + (r*R))
    print("Àrea = ", A)
    print("Volum = ", V)
def esfera(r):
    A = 4 * pi * pow(r,2)
    V = (4 * pi * pow(r,3))/3
    print("Àrea = ", A)
    print("Volum = ", V)
def piramide(b,n,a,ap,h):
    Pb = n * b   # perímetre de la base
    Ab = (Pb * a)/2 # àrea de la base
    A = (Pb * (a+ap))/2
    V = (Ab * h)/2
    print("Àrea = ", A)
    print("Volum = ", V)
def tetraedre(a):
    A = sqrt(3) * pow(a,2)
    V = (sqrt(2) * pow(a,3))/2
    print("Àrea = ", A)
    print("Volum = ", V)
def octaedre(a):
    A = 2 * sqrt(3) * pow(a,2)
    V = (sqrt(2) * pow(a,3))/3
    print("Àrea = ", A)
    print("Volum = ", V)
def tronc_piramide(b,n,bp,ap,a_piramide,h):
    Pb = n * b   # perímetre de la base major
    Ab = (Pb * a)/2 # àrea de la base major
    Pbp = n * bp # perímetre de la base menor
    Abp = (Pbp * ap)/2 # àrea de la base menor
    A = 0.5*(Pb+Pbp)*a_piramide + Ab + Abp
    V = (Ab + Abp + sqrt(Ab*Abp)) * h / 3
    print("Àrea = ", A)
    print("Volum = ", V)
def casquet(r,h):
    A = 2 * pi * r * h
    V = (pi * pow(h,2) * ((3 * r) - h))/3
    print("Àrea = ", A)
    print("Volum = ", V)
def falca(r,n):
    A = (4 * pi * pow(r,2) * n)/360
    V = (4 * pi * pow(r,3) * n)/(3*360)
    print("Àrea = ", A)
    print("Volum = ", V)
def zona_esferica(r,rg,rp,h):
    A = 2 * pi * r * h
    V = (pi * h * (pow(h,2) + 3*pow(rg,2) + 3*pow(rp,2)))/6
    print("Àrea = ", A)
    print("Volum = ", V)
    
# Programa principal main 
sortida = False
while not sortida:
    print("")
    print("Càlcul d'arees, volums i perímetres")
    print("Escull la figura a calcular:")
    print("1. quadrat")
    print("2. triangle")
    print("3. rectangle")
    print("4. paralelogram")
    print("5. rombe")
    print("6. estel")
    print("7. trapezi")
    print("8. cercle")
    print("9. polígon regular")
    print("10. corona")
    print("11. sector circular")
    print("12. cub")
    print("13. cilindre")
    print("14. ortoedre")
    print("15. prisma recte")
    print("16. con")
    print("17. tronc de con")
    print("18. esfera")
    print("19. piramide")
    print("20. tetraedre regular")
    print("21. octaedre regular")
    print("22. tronc de piràmide")
    print("23. casquet")
    print("24. falca esfèrica")
    print("25. zona esfèrica")
    print("26. sortir")
    
    opcio = int(input("Escull una opció: "))
    
    if opcio == 1: # quadrat
        print("Figura escollida: quadrat")
        a = float(input("costat a = "))
        quadrat(a)
    elif opcio ==2: # triangle
        print("Figura escollida: triangle")
        a = float(input("costat a = "))
        b = float(input("base, costat b = "))
        c = float(input("costat c = "))
        h = float(input("altura = "))
        triangle(a,b,c,h)
    elif opcio == 3: # rectangle
        print("Figura escollida: rectangle")
        a = float(input("costat a = "))
        b = float(input("costat b = "))
        rectangle(a,b)
    elif opcio == 4: # paral·lelogram
        print("Figura escollida: paralelogram")
        a = float(input("costat a = "))
        b = float(input("costat b = "))
        h = float(input("altura = "))
        paralelogram(a,b,h)
    elif opcio == 5: # rombe
        print("Figura escollida: rombe")
        D = float(input("diagonal major = "))
        d = float(input("diagonal menor = "))
        a = float(input("costat ="))
        rombe(D,d,a)
    elif opcio == 6: # estel
        print("Figura escollida: estel")
        D = float(input("diagonal major = "))
        d = float(input("diagonal menor = "))
        b = float(input("costat b = "))
        a = float(input("costat ="))
        estel(D,d,b,a)
    elif opcio == 7: # trapezi
        print("Figura escollida: trapezi")
        B = float(input("base gran = "))
        b = float(input("base petita = "))
        a = float(input("costat a = "))
        c = float(input("costat c = "))
        h = float(input("costat h = "))
        trapezi(B,b,a,c,h)
    elif opcio == 8: # cercle
        print("Figura escollida: cercle")
        r = float(input("radi = "))
        cercle(r)
    elif opcio == 9: # poligon
        print("Figura escollida: poligon")
        b = float(input("mida del costat = "))
        n = float(input("número de costats = "))
        a = float(input("apotema = "))
        poligon(b,n,a)
    elif opcio == 10: # corona circular
        print("Figura escollida: corona")
        R = float(input("radi major = "))
        r = float(input("radi menor = "))
        corona(R,r)
    elif opcio == 11: # sector circular
        print("Figura escollida: sector")
        r = float(input("radi = "))
        n = float(input("angle del sector en graus = "))
        sector(r,n)
    elif opcio == 12: # cub
        print("Figura escollida: cub")
        a = float(input("costat = "))
        cub(a)
    elif opcio == 13:  # cilindre
        print("Figura escollida: cilindre")
        r = float(input("radi = "))
        h = float(input("altura = "))
        cilindre(r,h)
    elif opcio == 14: # ortoedre
        print("Figura escollida: ortoedre")
        a = float(input("costat a = "))
        b = float(input("costat b = "))
        c = float(input("costat c = "))
        ortoedre(a,b,c)
    elif opcio == 15: # prisma recte
        print("Figura escollida: prisma")
        b = float(input("mida del costat = "))
        n = float(input("número de costats = "))
        a = float(input("apotema = "))
        h = float(input("altura = "))
        prisma(b,n,a,h)
    elif opcio == 16: # con
        print("Figura escollida: con")
        r = float(input("radi = "))
        g = float(input("generatriu = "))
        h = float(input("altura = "))
        con(r,g,h)
    elif opcio == 17: # tronc de con
        print("Figura escollida: tronc_con")
        r = float(input("radi menor = "))
        R = float(input("radi major = "))
        g = float(input("generatriu = "))
        h = float(input("altura = "))
        tronc_con(r,R,g,h)
    elif opcio == 18: # esfera
        print("Figura escollida: esfera")
        r = float(input("radi = "))
        esfera(r)
    elif opcio == 19: # piramide
        print("Figura escollida: piramide")
        b = float(input("mida del costat = "))
        n = float(input("número de costats = "))
        a = float(input("apotema de la base = "))
        ap = float(input("mida del triangle de la cara = "))
        h = float(input("altura de la piràmide = " ))
        piramide(b,n,a,ap,h)
    elif opcio == 20: # tetraedre regular
        print("Figura escollida: tetraedre")
        a = float(input("costat = "))
        tetraedre(a)
    elif opcio == 21: # octaedre regular
        print("Figura escollida: octaedre")
        a = float(input("costat = "))
        octaedre(a)
    elif opcio == 22: # tronc de piràmide
        print("Figura escollida: tronc_piramide")
        b = float(input("mida del costat major = "))
        n = float(input("número de costats = "))
        a = float(input("apotema de la base major = "))
        bp = float(input("mida del costat menor = "))
        ap = float(input("apotema de la base menor = "))
        a_piramide = float(input("mida de la cara del tronc de piràmide = "))
        h = float(input("altura = "))
        tronc_piramide(b,n,bp,ap,a_piramide,h)
    elif opcio == 23: # casquet
        print("Figura escollida: casquet")
        r = float(input("radi de l'esfera = "))
        h = float(input("altura del casquet = "))
        casquet(r,h)
    elif opcio == 24: # falca 
        print("Figura escollida: falca esfèrica")
        r = float(input("radi de l'esfera = "))
        n = float(input("angle de la falca en graus = "))
        falca(r,n)
    elif opcio == 25: # zona o segment esfèric
        print("Figura escollida: zona esfèrica")
        r = float(input("radi de l'esfera = "))
        rg = float(input("radi del segment gran = "))
        rp = float(input("radi del segment petit = "))
        h = float(input("altura de la zona esfèrica = "))
        zona_esferica(r,rg,rp,h)
    elif opcio == 26: # sortir
        print("Adeu! ")
        sortida = True
        
        
        
                  
        
        
        