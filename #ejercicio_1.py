#ejercicio_1

edad = int(input("ingrese su edad: "))

if edad > 0 and edad < 18:
    print(f"edad: {edad} ,tiene un descuento de un 50% ")
elif edad > 18 and edad < 30:
    print(f"edad: {edad} ,tiene un descuento de un 20% ")
elif edad  >= 60:
    print (f"edad: {edad} ,tiene un descuento de 90% ")
else:
    print(f"edad: {edad} ,no aplica descuento")       

