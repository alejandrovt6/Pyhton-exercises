import math
print("Cálculo de raíz cuadrada")
numero=int(input("Introduce un número por favor: "))

intentos=0

while numero<0:
    print("Incorrecto. Número negativo")

    if intentos==2:
        print("Demasiados intentos. Programa finalizado.")
        break;

    numero=int(input("Introduce un número por favor: "))
    if numero<0:
        intentos=intentos+1
    
if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es: " + str(solucion))