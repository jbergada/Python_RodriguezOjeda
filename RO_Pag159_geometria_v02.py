from RO_Pag159_geometria_v02 import *
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
    
    opcio = int(input("Escull una opció: "))
    
    if opcio == 1: # quadrat
        a = float(input("costat a = "))
        quadrat(a)
    elif opcio ==2: # triangle
        triangle(a,b,c,h)
    elif opcio == 3: # rectangle
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
        D = float(input("diagonal major = "))
        d = float(input("diagonal menor = "))
        a = float(input("costat ="))
        rombe(D,d,a)
    elif opcio == 6: # estel
        D = float(input("diagonal major = "))
        d = float(input("diagonal menor = "))
        b = float(input("costat b = "))
        a = float(input("costat ="))
        estel(D,d,b,a)
    elif opcio == 7: # trapezi
        B = float(input("base gran = "))
        b = float(input("base petita = "))
        a = float(input("costat a = "))
        c = float(input("costat c = "))
        h = float(input("costat h = "))
        trapezi(B,b,a,c,h)
    elif opcio == 8: # cercle
        r = float(input("radi = "))
        cercle(r)
    elif opcio == 9: # poligon
        b = float(input("mida del costat = "))
        n = float(input("número de costats = "))
        a = float(input("apotema = "))
        poligon(b,n,a)
    elif opcio == 10: # corona circular
        R = float(input("radi major = "))
        r = float(input("radi menor = "))
        corona(R,r)
    elif opcio == 11: # sector circular
        r = float(input("radi = "))
        n = float(input("angle del sector en graus = "))
        sector(r,n)
    elif opcio == 12: # cub
        a = float(input("costat = "))
        cub(a)
    elif opcio == 13:  # cilindre
        r = float(input("radi = "))
        h = float(input("altura = "))
        cilindre(r,h)
    elif opcio == 14: # ortoedre
        a = float(input("costat a = "))
        b = float(input("costat b = "))
        c = float(input("costat c = "))
        ortoedre(a,b,c)
    elif opcio == 15: # prisma recte
        b = float(input("mida del costat = "))
        n = float(input("número de costats = "))
        a = float(input("apotema = "))
        h = float(input("altura = "))
        prisma(b,n,a,h)
    elif opcio == 16: # con
        r = float(input("radi = "))
        g = float(input("generatriu = "))
        h = float(input("altura = "))
        con(r,g,h)
    elif opcio == 17: # tronc de con
        r = float(input("radi menor = "))
        R = float(input("radi major = "))
        g = float(input("generatriu = "))
        h = float(input("altura = "))
        tronc_con(r,R,g,h)
    elif opcio == 18: # esfera
        r = float(input("radi = "))
        esfera(r)
    elif opcio == 19: # piramide
        b = float(input("mida del costat = "))
        n = float(input("número de costats = "))
        a = float(input("apotema de la base = "))
        ap = float(input("mida del triangle de la cara = "))
        h = float(input("altura de la piràmide = " ))
        piramide(b,n,a,ap,h)
    elif opcio == 20: # tetraedre regular
        a = float(input("costat = "))
        tetraedre(a)
    elif opcio == 21: # octaedre regular
        a = float(input("costat = "))
        octaedre(a)
    elif opcio == 22: # tronc de piràmide
        b = float(input("mida del costat major = "))
        n = float(input("número de costats = "))
        a = float(input("apotema de la base major = "))
        bp = float(input("mida del costat menor = "))
        ap = float(input("apotema de la base menor = "))
        a_piramide = float(input("mida de la cara del tronc de piràmide = "))
        h = float(input("altura = "))
        tronc_piramide(b,n,bp,ap,a_piramide,h)
    elif opcio == 23: # casquet
        pass
    elif opcio == 26: # acabar
        sortida = True
        
        