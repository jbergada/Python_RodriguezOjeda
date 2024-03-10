#RO_095_09_if_triangles.py

costat1= float(input("costat1 = "))
costat2= float(input("costat2 = "))
costat3= float(input("costat3 = "))

if costat1 == costat2 and costat2 == costat3:
    print("triangle equilàter")
elif costat1 == costat2 and costat2 != costat3:
    print("triangle isòsceles ")
elif costat1 == costat3 and costat3 != costat2:
    print("triangle isòsceles ")
elif costat2 == costat3 and costat3 != costat1:
    print("triangle isòsceles ")
elif costat1 != costat2 and costat2 != costat3:
    print("triangle escalè ")
    

