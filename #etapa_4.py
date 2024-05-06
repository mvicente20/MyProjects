#etapa_4

def pregunta_animal():
    respuesta = input("¿Cuál de los siguientes animales vive en el agua?\n"
                      "a) Perro\n"
                      "b) Cocodrilo\n"
                      "c) Conejo\n"
                      "d) Tiburón\n")
    respuesta = respuesta.lower()

    puntaje = 0
    if respuesta == "b":
        puntaje += 0.5
    elif respuesta == "d":
        puntaje += 1.0

    print("Puntaje obtenido:", puntaje)

pregunta_animal()