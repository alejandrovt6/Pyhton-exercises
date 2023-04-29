# OPCION 1
email=input("Introduce tu correo: ")
arroba=email.count('@')

if(arroba!=1 or email.rfind("@")==(len(email)-1) or email.find("@")==0):
    print("Email incorrecto")
else:
    print("Email correcto")




