
try:
    # Solicitar al usuario dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Dividir el primer número por el segundo número
    resultado = num1 / num2

    # Imprimir el resultado de la división
    print("El resultado de la división es:", resultado)

# Capturar errores de valor
except ValueError:
    print("Error: Ha ingresado un valor no válido. Por favor, ingrese solo números.")

# Capturar errores de división por cero
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero. Por favor, ingrese un segundo número distinto de cero.")

# Capturar cualquier otro error
except Exception as e:
    print("Ocurrió un error:", e)