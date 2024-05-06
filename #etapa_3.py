#etapa_3

def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Solicitar las notas al usuario
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# Calcular el promedio de las notas
notas = [nota1, nota2, nota3]
promedio = calcular_promedio(notas)

# Determinar si el estudiante aprobó o no
if promedio >= 4.0:
    print("Aprobado")
else:
    print("Desaprobado")