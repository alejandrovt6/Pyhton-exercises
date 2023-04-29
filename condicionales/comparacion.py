salarioPresidente=int(input("Salario presidente "))
# print("Salario presidente: " + str(salarioPresidente))

salarioDirector=int(input("Salario director "))
# print("Salario director: " + str(salarioDirector))

salarioJefeArea=int(input("Salario Jefe Área "))
# print("Salario Jefe Área: " + str(salarioJefeArea))

salarioAdministrativo=int(input("Salario Administrativo "))
# print("Salario Administrativo: " + str(salarioAdministrativo))

if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")