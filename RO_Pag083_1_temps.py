#RO_Pag083_1_temps


print("Versió 1 amb una funció")
print("=======================")
print("                       ")

DIES_ANY = 365
DIES_MES = 30

def get_next_step(data, ct):
    next_step = data // ct
    rest = data % ct
    return (next_step, rest)

dies = 1372

anys, dies_rest = get_next_step(dies, DIES_ANY)
mes, dies_final = get_next_step(dies_rest, DIES_MES)

print("anys = ", anys)
print("mes = ", mes)
print("dies = ", dies_final)

print("                       ")
print("Versió 2 amb una funció")
print("=======================")
print("                       ")

dies = 1372
anys = dies // 365

dies_restants = dies % 365

mes = dies_restants // 30

dies_restants_2 = dies_restants % 30

print("anys = ", anys)
print("mes = ", mes)
print("dies = ", dies_restants_2)

print("                       ")
print("Versió 3 amb una funció")
print("=======================")
print("                       ")

dies = 1372
anys = dies / 365
anys_sencers = dies // 365
anys_no_sencers = anys - anys_sencers

dies_anys_no_sencers = anys_no_sencers * 365

mesos_dies_anys_no_sencers = dies_anys_no_sencers / 30

mesos_sencers = int(dies_anys_no_sencers // 30)

mesos_no_sencers = mesos_dies_anys_no_sencers - mesos_sencers

dies_mesos_no_sencers = int(mesos_no_sencers * 30)


print("anys = ", anys_sencers)
print("mes = ", mesos_sencers)
print("dies = ", dies_mesos_no_sencers)

