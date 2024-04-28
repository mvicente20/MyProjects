def es_numero_par_o_impar(numero):
    if numero % 2 == 0:
         return "par"
    else:
         return "impar"
    

def main():
    try:    
          numero = int(input("Por favor, introduce un numero entero: "))
          resultado = es_numero_par_o_impar(numero)
          print("el numero es" ,numero , "es" , resultado)
    except ValueError:
         print("Error: Por favor, introduce un numero entero valido. ") 

if __name__ == "__main__":
    main()              