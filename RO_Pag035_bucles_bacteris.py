# RO_Pag035_bucles_bacteris.py

bacteris = int(input("Nombre de bacteris = "))
bacteris_max = int(input("Nombre de bactertis màxim = "))

dies = 0

while bacteris <= bacteris_max :
    bacteris = 2 * bacteris
    dies = dies + 1
    print(bacteris)
print("dies fins a arribar al nombre màxim de bacgteris = ", dies)