#etapa_1

def verificar_edad(edad):
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

# Solicitar la edad al usuario
edad = int(input("Ingresa tu edad: "))
verificar_edad(edad)