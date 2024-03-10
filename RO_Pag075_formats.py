#RO_Pag075_formats.py

n = 23
x = 7.78925
e = "ESPOL"

print("Prova %5d %8.2f %10s"%(n,x,e))

f = "Prova %5d %8.2f %10s"
print(f%(n,x,e))

print("Prova {0:5}{1:9.3}      {2:10.5}".format(n,x,e))
