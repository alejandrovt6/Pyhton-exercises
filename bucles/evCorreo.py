email=False
for e in "alejandro@correo.es":
    if(e=="@"):
        email=True
if email==True:   # Con solo "if email:" da por hecho True
    print("Email correcto")
else:
    print("Email incorrecto")

