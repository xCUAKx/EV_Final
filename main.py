import random

import juego

nombre=juego.inicio_nombre()
puntos = 0
comodin_usado = False

for all_preguntas in juego.obtener_preguntas():
    pregunta = all_preguntas['question']
    respuestas_correcta = all_preguntas['correct_answer']
    respuestas_incorrecta = all_preguntas['incorrect_answers']

    opciones = respuestas_incorrecta # opciones = respuestas_incorrectas + [respuesta_correcta]
    opciones.append(respuestas_correcta)
    random.shuffle(opciones)

    juego.mostrar_pregunta(pregunta,opciones)
    comodin=input(f"Usamos el comodin {nombre}?")
    #juego.responder(respuestas_correcta)
    if comodin_usado:
        print("No quedan comodines")
    elif comodin == "si":
        print("Comodin usado")
        comodin_usado = True
        continue

    respuesta_usuario = input(f"Introduce tu respuesta: ")
    if respuesta_usuario == respuestas_correcta:
        puntos += 1
        print(f"CORRECTO! Puntos: {puntos}")

    else:
        print("GAME OVER")
        break

