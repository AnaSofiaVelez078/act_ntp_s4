import random
import math

# Función que genera una tupla con coordenadas (x, y) de 10 puntos aleatorios
# y calcula cuáles están dentro de un círculo de radio 5 centrado en el origen (0,0)
def puntos_dentro_circulo():
    # Generar una tupla con 10 puntos aleatorios
    puntos = tuple(
        (random.uniform(-10, 10), random.uniform(-10, 10))  # Coordenadas x, y entre -10 y 10
        for _ in range(10)
    )

    print("Puntos generados (x, y):")
    for punto in puntos:
        print(punto)

    # Radio del círculo
    radio = 5

    # Lista para almacenar puntos dentro del círculo
    puntos_en_circulo = []

    # Recorrer los puntos con un ciclo for
    for x, y in puntos:
        # Calcular la distancia al origen usando la fórmula de la distancia euclidiana
        distancia = math.sqrt(x**2 + y**2)

        # Verificar si el punto está dentro del círculo (distancia <= radio)
        if distancia <= radio:
            puntos_en_circulo.append((x, y))

    print("\nPuntos dentro del círculo de radio 5:")
    for punto in puntos_en_circulo:
        print(punto)

    # Retornar la tupla con todos los puntos y la lista de los que están dentro del círculo
    return puntos, puntos_en_circulo

# Ejecutar la función
puntos, dentro = puntos_dentro_circulo()
