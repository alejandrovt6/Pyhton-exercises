from tkinter import *

root=Tk()

miFrame=Frame(root, width="500", height="400")
miFrame.pack()

miImagen=PhotoImage(file="graficos/gato.png")

# PARA TEXTO
#Label(miFrame, text="Hola como estais",fg="blue",font=("Comic Sans MS",18)).place(x=100,y=200)

Label(miFrame,image=miImagen).place(x=100,y=200)



root.mainloop()