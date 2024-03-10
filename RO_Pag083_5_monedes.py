#RO_Pag083_5_monedes.py

euros = 2564

bitllets_100 = euros // 100
euros_sobrants = euros % 100

bitllets_50 = euros_sobrants // 50
euros_sobrants = euros_sobrants % 50

bitllets_20 = euros_sobrants//20
euros_sobrants = euros_sobrants % 20

bitllets_10 = euros_sobrants//10
euros_sobrants = euros_sobrants % 10

bitllets_5 = euros_sobrants//5
euros_sobrants = euros_sobrants % 5

monedes_1 = euros_sobrants

print(bitllets_100, " bitllets de 100 ")
print(bitllets_50, "bitllets de 50 ")
print(bitllets_20, "bitllets de 20 ")
print(bitllets_10, "bitllets de 10 ")
print(bitllets_5, "bitllets de 5 ")
print(monedes_1, "monedes d'un € ")