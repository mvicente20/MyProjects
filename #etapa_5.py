#etapa_5

def formulario_preguntas_alternativo():
    puntaje_total = 0
    
    # Pregunta 1
    respuesta1 = input("¿Cuál es el río más largo del mundo?\n"
                       "a) Nilo\n"
                       "b) Amazonas\n"
                       "c) Yangtsé\n"
                       "d) Mississippi\n")
    if respuesta1.lower() == "b":
        puntaje_total += 1
    
    # Pregunta 2
    respuesta2 = input("¿Quién pintó la Mona Lisa?\n"
                       "a) Leonardo da Vinci\n"
                       "b) Pablo Picasso\n"
                       "c) Vincent van Gogh\n"
                       "d) Claude Monet\n")
    if respuesta2.lower() == "a":
        puntaje_total += 1
    
    # Pregunta 3
    respuesta3 = input("¿Cuál es el planeta más grande del sistema solar?\n"
                       "a) Tierra\n"
                       "b) Júpiter\n"
                       "c) Saturno\n"
                       "d) Neptuno\n")
    if respuesta3.lower() == "b":
        puntaje_total += 1
    
    # Mostrar puntaje obtenido
    print("Puntaje obtenido:", puntaje_total)

formulario_preguntas_alternativo()