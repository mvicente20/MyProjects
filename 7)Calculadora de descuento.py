def calcular_precio_final(precio_original, porcentaje_descuento):
    # Calcula el descuento
    descuento = precio_original * (porcentaje_descuento / 100)
    # Calcula el precio con descuento
    precio_con_descuento = precio_original - descuento
    # Calcula el IVA (16%)
    iva = precio_con_descuento * 0.16
    # Calcula el precio final con IVA
    precio_final = precio_con_descuento + iva
    return precio_con_descuento, precio_final, iva

# Solicita al usuario el precio original
precio_original = float(input("Ingresa el precio original del producto: "))

# Define el porcentaje de descuento
porcentaje_descuento = 40

# Calcula el precio final y el subtotal
precio_con_descuento, precio_final, iva = calcular_precio_final(precio_original, porcentaje_descuento)

# Imprime los resultados
print("Subtotal (sin IVA):", precio_con_descuento)
print("IVA (16%):", iva)
print("Total (con IVA):", precio_final)