#ejercicio_3

user = input("ingrese su user: ")
pwd = input("ingrese su password: ")

if user == "duoc" and pwd == "123duoc":
    valordev = int(input("bienvenido, ingrese el valor a devolver: "))
    if valordev > 100000:
     print("se dara la maxima urgencia a su devolucion de dinero")
    else:
     print("el caso ha quedado registrado le informaremos lo antes posible")
else:
  print("error de contraseña")


  