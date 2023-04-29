from tkinter import *

raiz=Tk()

raiz.title("Entrys") 

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()
midir=StringVar()

# CUADROS

# cuadroTexto=Entry(miFrame)
# #cuadroTexto.place(x=100,y=100)
# cuadroTexto.grid(row=0,column=1)

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0,column=1, pady=10, padx=10)
cuadroNombre.config(fg="red", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1, pady=10, padx=10)

cuadroDireccion=Entry(miFrame, textvariable=midir)
cuadroDireccion.grid(row=2,column=1, pady=10, padx=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3,column=1, pady=10, padx=10)
cuadroPass.config(show="@")
# puedes poner el caracter que quieras

textoComentario=Text(miFrame, width=16,height=5)
textoComentario.grid(row=4,column=1, pady=10, padx=10)

scrollV=Scrollbar(miFrame,command=textoComentario.yview)
scrollV.grid(row=4,column=2, sticky="nsew")
# adapta el scroll
textoComentario.config(yscrollcommand=scrollV.set)
# indica donde estás en todo momento

# LABELS

nombreLabel=Label(miFrame,text="Nombre: ")
#nombreLabel.place(x=100,y=100) # lo coloca al lado si tiene la misma X
nombreLabel.grid(row=0,column=0, sticky="e", pady=10, padx=10) 
# sticky: alinear east,west,north,south

apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=1,column=0, sticky="e", pady=10, padx=10)

direccionLabel=Label(miFrame,text="Dirección: ")
direccionLabel.grid(row=2,column=0, sticky="e", pady=10, padx=10)

passLabel=Label(miFrame,text="Password: ")
passLabel.grid(row=3,column=0, sticky="e", pady=10, padx=10)

comentsLabel=Label(miFrame,text="Comentario: ")
comentsLabel.grid(row=4,column=0, sticky="e", pady=10, padx=10)

def codigoBoton():
    minombre.set("Ale")
    midir.set("Calle x")

botonEnvio=Button(raiz,text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()