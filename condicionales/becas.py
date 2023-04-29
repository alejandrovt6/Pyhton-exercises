print("Programa de becas")

distancia=int(input("Introduce la distancia al centro en km: "))
# print(distancia)

nHermanos=int(input("Introduce el número de hermanos: "))
# print(nHermanos)

renta=int(input("Introduce la renta bruta anual: "))
# print(renta)

if distancia>40 and nHermanos>2 or renta<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")