def invertir_cadena(cadena):
    #Utilizamos el slicing para invertir la cadena
    cadena_invertida = cadena[::-1]
    return cadena_invertida


def main():
    #solicitar al usuario una cadena de texto
    
    cadena_original = input ("Por favor, Ingresa una cadena de texto: ")
    
    #se invierte la cadena
    
    cadena_invertida = invertir_cadena(cadena_original)

    #se imprime la cadena invertida

    print("la cadena invertida es: ", cadena_invertida)

if __name__ == "__main__":
    main()   