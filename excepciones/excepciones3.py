def evEdad(edad):
    if edad<0:
        raise TypeError("Edad negativa no válida")
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate..."
    
print(evEdad(100))
