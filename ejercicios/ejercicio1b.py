# OPCION 2
def validar_email(email):
    if email.count('@') == 1 and email.index('@') != 0 and email.index('@') != len(email) - 1:
        print("La dirección de email es correcta")
    else:
        print("La dirección de email es incorrecta")

email = input("Introduce una dirección de email: ")
validar_email(email)