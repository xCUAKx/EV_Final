# url de la API https://opentdb.com/api.php?amount=15&difficulty=medium&type=multiple
import time
import requests

def inicio_nombre():
    print("Bienvenido a quien quiere ser MILLONARIO!!\n")
    nombre = input("Escribe tu nombre: ")
    print(f"El juego va a comenzar {nombre}...")
    time.sleep(3)
    return nombre

def obtener_preguntas():
    respuesta = requests.get("https://opentdb.com/api.php?amount=15&difficulty=medium&type=multiple")
    preguntas = respuesta.json()['results']
    return preguntas

"""def responder(respuesta):
    puntos = 0
    respuesta_usuario = input(f"Introduce tu respuesta: ")
    if respuesta_usuario == respuesta:
        puntos += 1
        print(f"CORRECTO! Puntos: {puntos}")
    else:
        print("GAME OVER")"""

def mostrar_pregunta(pregunta, opciones):
    print(f"{pregunta}")
    for o in opciones:
        print("\t" + o)

