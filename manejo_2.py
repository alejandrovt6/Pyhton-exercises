from io import open

archivo_texto = open("archivo.txt", "r") 
# r+ : lectura y escritura

print(archivo_texto.read())

# archivo_texto.seek(11)
# print(archivo_texto.read())
# archivo_texto.close()

archivo_texto.seek(len(archivo_texto.read())/2)
