def verificar_contrasena(contraseña):
    # Verificamos la longitud de la contraseña
    if len(contraseña) < 8:
        return False
    
    # Verificamos si hay al menos una letra mayúscula, una minúscula y un número
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    
    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
    
    # Devolvemos True si cumple con todos los requisitos, False en caso contrario
    return tiene_mayuscula and tiene_minuscula and tiene_numero

# Solicitamos al usuario que ingrese una contraseña
contraseña = input("Por favor, ingresa una contraseña: ")

# Verificamos si la contraseña cumple con los requisitos y mostramos un mensaje adecuado
if verificar_contrasena(contraseña):
    print("La contraseña cumple con los requisitos.")
else:
    print("La contraseña no cumple con los requisitos.")