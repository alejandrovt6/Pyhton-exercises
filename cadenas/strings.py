nombreUsu=input("Introduce tu nombre de usuario: ")
print("El nombre es: ", nombreUsu.upper())
print("El nombre es: ", nombreUsu.lower())
print("El nombre es: ", nombreUsu.capitalize())

edad=input("Introduce tu edad: ")

while(edad.isdigit()==False):
    print("Introduce un número ")
    edad=input("Introduce tu edad: ")
    
if(int(edad)<18):
    print("No puede pasar")
else:
    print("Puede pasar")