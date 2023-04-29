mitupla=("Juan", 13, 1, 1995) # Paréntesis son opcionales
nombre, dia, mes, anho=mitupla # Asigna por orden a las variables
print(nombre)
print(anho)

print(mitupla[2])

milista=list(mitupla)
print(mitupla)
print(milista)
print("Manolo" in mitupla) # True o false
print(mitupla.count(13)) # Cuenta las veces que está el elemento
print(len(mitupla)) # Longitud de la tupla

# LAS TUPLAS NO SE PUEDEN MODIFICAR (AÑADIR, BORRAR...)