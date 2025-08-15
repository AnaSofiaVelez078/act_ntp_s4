import math

# Función que recibe una tupla de puntos (x, y)
# y calcula la distancia total recorrida al visitar los puntos en orden
def distancia_total(puntos):
    # Variable para acumular la distancia total
    distancia = 0.0

    # Recorremos la tupla de puntos usando índices para calcular distancias entre puntos consecutivos
    for i in range(len(puntos) - 1):
        x1, y1 = puntos[i]
        x2, y2 = puntos[i + 1]

        # Calculamos la distancia euclidiana entre dos puntos
        d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        distancia += d  # Acumulamos la distancia

    return distancia

# Tupla de prueba con puntos (x, y)
puntos = ((0, 0), (3, 4), (6, 8), (9, 12))

# Calculamos y mostramos la distancia total recorrida
total = distancia_total(puntos)
print(f"Distancia total recorrida: {total:.2f}")
