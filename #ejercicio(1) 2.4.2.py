#ejercicio_2.4.2

try:

    cantidad_bultos = int(input("Ingrese la cantidad de bultos: "))
    if cantidad_bultos <= 0:
        raise ValueError("La cantidad de bultos debe ser un número positivo.")

    total_pago_livianos = 0
    total_pago_normales = 0
    contador_livianos = 0
    contador_normales = 0

    for i in range(cantidad_bultos):
        peso_bulto = float(input(f"Ingrese el peso del bulto {i+1}: "))
        if peso_bulto <= 0:
            raise ValueError("El peso del bulto debe ser un número positivo.")
        elif peso_bulto <= 5:
            total_pago_livianos += 1000
            contador_livianos += 1
        else:
            total_pago_normales += 2000
            contador_normales += 1

    print(f"{contador_livianos} bulto{'s' if contador_livianos > 1 else ''} liviano{'s' if contador_livianos > 1 else ''} ${total_pago_livianos}")
    print(f"{contador_normales} bulto{'s' if contador_normales > 1 else ''} normal{'es' if contador_normales > 1 else ''} ${total_pago_normales}")
    print(f"Valor total a pagar: ${total_pago_livianos + total_pago_normales}")

except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("Ocurrió un error:", e)