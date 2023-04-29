contador=0
miemail=input("Introduce tu email: ")

for i in miemail:
    if(i=="@" or i=="."):
        contador=contador+1
if contador==2:
    print("Es correcto")
else:
    print("No es correcto")