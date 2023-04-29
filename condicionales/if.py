print("Programa de evaluación de notas de alumnos")

# Introducir valor String
notaAlumno=input("Introduce la nota del alumno: ") 

def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Suspenso"

    return valoracion

print(evaluacion(int(notaAlumno)))
# int para que detecte que es número