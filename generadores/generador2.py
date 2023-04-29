def generaPares(limite):
    num=1

    while num<limite:
        yield num*2
        num=num+1

devuelvePares=generaPares(10)

# Devuelve lista entera 
# for i in devuelvePares:
#    print(i)

# Devuelve x primeros elementos . En este caso 3
print(next(devuelvePares))
print("Aquí puede ir más código... ")
print(next(devuelvePares))
print("Aquí puede ir más código... ")
print(next(devuelvePares))
