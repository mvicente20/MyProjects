# Función para leer el archivo de ventas
def leer_ventas(archivo):
    ventas = []
    with open(archivo, 'r') as file:
        for line in file:
            ventas.append([int(x) for x in line.strip().split(',')])
    return ventas

# Función para calcular el total de ventas para cada producto y el promedio de ventas diarias
def analizar_ventas(ventas):
    total_por_producto = [0] * len(ventas[0])
    total_ventas_diarias = 0
    dias_con_ventas = len(ventas)
    
    for dia in ventas:
        total_ventas_diarias += sum(dia)
        for i, cantidad in enumerate(dia):
            total_por_producto[i] += cantidad
    
    promedio_ventas_diarias = total_ventas_diarias / dias_con_ventas
    return total_por_producto, promedio_ventas_diarias

# Función para imprimir los resultados
def imprimir_resultados(total_por_producto, promedio_ventas_diarias):
    print("Total de ventas por producto:")
    for i, total in enumerate(total_por_producto):
        print(f"Producto {i+1}: {total}")
    print(f"\nPromedio de ventas diarias: {promedio_ventas_diarias:.2f}")

# Nombre del archivo de ventas
archivo_ventas = "ventas.txt"

# Leer el archivo de ventas
ventas = leer_ventas(archivo_ventas)

# Analizar las ventas
total_por_producto, promedio_ventas_diarias = analizar_ventas(ventas)

# Imprimir los resultados
imprimir_resultados(total_por_producto, promedio_ventas_diarias)