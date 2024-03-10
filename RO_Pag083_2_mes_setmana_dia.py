#RO_Pag083_2_mes_setmana_dia.py

dies = 175
mesos = dies//30
dies_sobrants = dies%30
setmanes = dies_sobrants // 7

dies_sobrants = dies_sobrants % 7

print("mesos = ", mesos, "setmanes = ", setmanes, "dies = ", dies_sobrants)