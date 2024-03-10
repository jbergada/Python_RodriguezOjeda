# RO_Pag032_decisions4.py

altura = float(input("altura = "))
amplada = float(input("amplada = "))
profunditat = float(input("profunditat = "))

diag_altura_amplada = (altura * altura + amplada * amplada) ** 0.5 # diagonal de l'alçat
diag_altura_profunditat = (altura * altura + profunditat * profunditat) ** 0.5 # diagonal del perfil
diag_amplada_profunditat = (amplada * amplada + profunditat * profunditat) ** 0.5 # diagonal de la base

if diag_altura_amplada >= diag_altura_profunditat :
    if diag_altura_amplada >= diag_amplada_profunditat:
        print("La diagonal major és la de l'alçat ", diag_altura_amplada)

elif diag_altura_profunditat >= diag_altura_amplada:
    if diag_altura_profunditat >= diag_amplada_profunditat:
        print("La diagonal major és la del perfil ", diag_altura_profunditat)
    else:
        print("La diagonal major és la de la base ", diag_amplada_profunditat)
