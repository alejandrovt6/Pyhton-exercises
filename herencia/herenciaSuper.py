class Persona():
    def __init__ (self,nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad, 
            "Residencia: ", self.lugar_residencia)
    
class Empleado(Persona):
    def __init__ (self,salario,antiguedad, nombre_e, edad_e, lugar_e):
        super().__init__(nombre_e,edad_e,lugar_e)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario,"Antiguedad: ",self.antiguedad)

Manuel=Empleado(1500,15,"Manuel",55,"España")
Manuel.descripcion()

print(isinstance(Manuel,Persona))
print(isinstance(Manuel,Empleado))




