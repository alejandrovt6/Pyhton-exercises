edad=int(input("Introduce la edad por favor: "))

while edad<5 or edad<100:
    print("Edad incorrecta. Vuelve a intentarlo")
    edad=int(input("Introduce la edad por favor: "))

print("Gracias. Puedes pasar")
print("Edad: " + str(edad))
