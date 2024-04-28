def calcular_imc(peso, altura):
    """
    Calcula el índice de masa corporal (IMC) utilizando la fórmula IMC = peso / (altura ** 2).
    """
    imc = peso / (altura ** 2)
    
    return imc
def main():
    
    # Solicitar al usuario su peso en kilogramos
    peso = float(input("ingresa tu peso en kilogramos: "))
    
    # Solicitar al usuario su altura en kilogramos
    altura = float(input("ingresa tu altura en metros: "))
    
    # Calcular el IMC
    imc = calcular_imc(peso, altura)


    # Imprimir el resultado de IMC con 2 decimales
    print("tu indice de masa corporal (IMC) es {:.2f}" .format(imc))

if __name__ == "__main__":
    main()    

