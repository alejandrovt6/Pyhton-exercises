print("Asignaturas optativas")

print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura: ")

asignatura=opcion.lower() # Para minúsculas FALLA

if asignatura in ("Informática gráfica", "Pruebas de software", "Usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("Asignatura incorrecta")

