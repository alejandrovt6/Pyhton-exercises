milista=["Maria", "Pepe", "Marta", "Antonio", 54.2, False] 
# Empieza desde 0
# Almacena distintos tipos

milista.append("Sandra") # Añade al final
milista.insert(2, "Fernando") # Índice, nombre
milista.extend(["Alejandro", "Lucia"]) # Concatena la lista
milista.remove("Maria") # Elimina
milista.pop() # Elimina el último

print(milista[:]) # Todos
print(milista[2]) # Un elemento
print(milista[-1]) # Cuenta inversa
print(milista[0:2]) # El último no se incluye
print(milista.index("Antonio")) # Devuelve el índice
print("Pepe" in milista) # True o false

milista2=["Isa", "Cristian"]

milista3=milista+milista2 # Suma listas
print(milista3[:]) 