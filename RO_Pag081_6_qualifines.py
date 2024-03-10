#RO_Pag081_6_qualifines.py

repte = float(input("quali del repte sobre 100 punts= "))
tema = float(input("quali del tema sobre 10 punts= "))
tasca1 = float(input("quali de la tasca1 sobre 10 punts= "))
tasca2 = float(input("quali de la tasca2 sobre 10 punts= "))
tasca3 = float(input("quali de la tasca3 sobre 10 punts= "))

repte = repte/10

tasca = (tasca1+tasca2+tasca3)/3

qualifine = 0.7*repte + 0.2*tema + 0.1*tasca
print("qualifine = ",qualifine) 