#etapa_2

def validar_credenciales(usuario, contraseña):
    usuarios = {"pedro": "1234", "angel": "a4s1"}
    if usuario in usuarios and usuarios[usuario] == contraseña:
        return True
    else:
        return False

# Solicitar usuario y contraseña al usuario
usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

if validar_credenciales(usuario, contraseña):
    print("Acceso concedido.")
else:
    print("Credenciales incorrectas.")