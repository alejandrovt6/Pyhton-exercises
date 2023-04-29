class Coche():

    def __init__(self): # Constructor , estado inicial
        # Propiedades
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4  # __ Encapsulación, no accesible desde fuera de la clase
        self.__enmarcha=False

    # Comportamientos
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequeoI=self.__chequeo()
            
        if(self.__enmarcha and chequeoI):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeoI==False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene ",self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ",
            self.__largoChasis)
    
    def __chequeo(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

# Instanciación de clase
# Objeto = Clase()
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()
# Si se cambia el estado de aceite, gasolina o puertas, dirá que ha ido mal

# self es como this en Java

# SEGUNDO OBJETO
miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
