from tkinter import *

raiz=Tk() 
# Construir raiz
raiz.title("Ventana pruebas") 
#raiz.resizable(1,1) 
# width, height. 0 = no se puede redimensionar al abrir
# También funciona con false y true

raiz.iconbitmap("graficos/1.ico")
# Agregar una etiqueta y un botón para cerrar la ventana
#raiz.geometry("650x350")
# Ancho y alto
raiz.config(bg="blue")
# Color fondo

miFrame=Frame()
miFrame.pack()
#miFrame.pack(side="right", anchor="n") 
# side: right, left, bottom, top
# anchor: (n)orth, (s)outh, (w)est, (e)ast
#miFrame.pack(fill="y", exapnd="False")
# fill: rellena a x, y, both

miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
miFrame.config(relief="groove") # borde
miFrame.config(cursor="pirate")

raiz.mainloop() 
# Bucle para estar a la escucha
# mainloop siempre al final

# .pyw la abre sin la consola detrás





