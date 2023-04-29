from io import open

# archivo_texto=open("archivo.txt","w")

# frase="estupendo dia para estudiar python \n el miercoles"
# archivo_texto.write(frase)
# archivo_texto.close()

archivo_texto = open("archivo.txt", "r")

texto = archivo_texto.read()
archivo_texto.close()
print(texto)

# lineas_texto=archivo_texto.readlines()
# print(lineas_texto[1])
# archivo_texto.close()

# w write, r read, a append
# append añade información con write
archivo = open("mi_archivo.txt", "a")
archivo.write("Esta es una nueva línea que se agregará al final del archivo.\n")
archivo.close()