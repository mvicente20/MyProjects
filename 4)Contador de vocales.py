def contar_vocales(cadena):
    #iniciaremos un contador para las vocales
    contador_vocales = 0
    #definimos una lista de vocales
    vocales = ['a', 'e', 'i', 'o', 'u']

    #Recorremos la cadena de texto
    for caracter in cadena:
        # Si el caracter esta en la lista de vocales, aumentamos el contador
        if caracter.lower() in vocales:
            contador_vocales += 1

    return contador_vocales

# Solicitamos al usuario que ingrese una cadena de texto
cadena = input("Por favor, ingresa una cadena de texto: ")

# Llamamos a la función contar_vocales y almacenamos el resultado
cantidad_vocales = contar_vocales(cadena)

# Imprimimos el resultado
print("La cantidad de vocales en la cadena es:", cantidad_vocales)        