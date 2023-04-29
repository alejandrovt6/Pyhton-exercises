# clave : valor
midiccionario={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
midiccionario["Italia"]="Lisboa" # Erróneo
print(midiccionario["Francia"])
print(midiccionario)

midiccionario["Italia"]="Roma" # Sobreescribir
print(midiccionario)

del midiccionario["Reino Unido"]
print(midiccionario)


mitupla=("España", "Francia", "Reino Unido")
midiccionario={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres"}
print(midiccionario["Francia"])

midiccionario2={23:"Jordan", "Anillos:":[1991,1992,1993]}
print(midiccionario2["Anillos:"])
print(midiccionario2.keys())
print(midiccionario2.values())