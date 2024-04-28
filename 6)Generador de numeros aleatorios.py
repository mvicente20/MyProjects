import random

def generar_numeros_aleatorios():
    # Genera dos números aleatorios entre 1 y 100
    numero1 = random.randint(1, 100)
    numero2 = random.randint(1, 100)
    return numero1, numero2

def adivinar_suma():
    # Genera los números aleatorios
    numero1, numero2 = generar_numeros_aleatorios()
    
    # Solicita al usuario que adivine la suma
    suma_adivinada = int(input(f"Adivina la suma de {numero1} y {numero2}: "))
    
    # Calcula la suma correcta
    suma_correcta = numero1 + numero2
    
    # Compara la respuesta del usuario con la suma correcta e imprime el resultado
    if suma_adivinada == suma_correcta:
        print("¡Correcto! La suma es", suma_correcta)
    else:
        print("Incorrecto. La suma correcta es", suma_correcta)

# Llama a la función para que el usuario juegue
adivinar_suma()